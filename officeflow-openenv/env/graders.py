from env.models import Action, OfficeState, Reward


def grade_action(action: Action, state: OfficeState, result: str, cumulative: float) -> Reward:
    """Assign reward based on action quality and outcome."""
    value = 0.0
    reason = result

    if "error" in result.lower() or "not found" in result.lower():
        value = -0.5
        return Reward(value=value, reason=reason, cumulative=cumulative + value)

    if action.action_type == "read_email":
        value = 0.1

    elif action.action_type == "classify_email":
        email = next((e for e in state.emails if e.id == action.target_id), None)
        if email and action.classification == email.category:
            value = 0.5  # correct classification
        elif email:
            value = -0.2  # wrong classification

    elif action.action_type == "reply_email":
        email = next((e for e in state.emails if e.id == action.target_id), None)
        if email and email.category == "urgent":
            value = 1.0  # replying urgent emails is high value
        elif email and email.category == "spam":
            value = -0.5  # replying spam is bad
        else:
            value = 0.3

    elif action.action_type == "ignore_email":
        email = next((e for e in state.emails if e.id == action.target_id), None)
        if email and email.category == "spam":
            value = 0.5  # correctly ignoring spam
        elif email and email.category == "urgent":
            value = -1.0  # ignoring urgent is very bad
        else:
            value = -0.1

    elif action.action_type == "schedule_meeting":
        meeting = next((m for m in state.meetings if m.id == action.target_id), None)
        if meeting and not meeting.conflict:
            value = 0.5
        elif meeting and meeting.conflict:
            value = -0.3  # scheduling conflicting meeting

    elif action.action_type == "resolve_conflict":
        value = 0.8  # resolving conflicts is valuable

    elif action.action_type == "add_task":
        value = 0.2

    elif action.action_type == "complete_task":
        task = next((t for t in state.tasks if t.id == action.target_id), None)
        if task and task.priority == "high":
            value = 1.5
        elif task and task.priority == "medium":
            value = 0.8
        else:
            value = 0.4

    return Reward(value=value, reason=reason, cumulative=cumulative + value)


def compute_final_score(state: OfficeState) -> float:
    """Compute end-of-episode bonus/penalty."""
    bonus = 0.0

    # Bonus for completing high-priority tasks
    for task in state.tasks:
        if task.completed and task.priority == "high":
            bonus += 2.0
        elif task.completed and task.priority == "medium":
            bonus += 1.0

    # Penalty for unread urgent emails
    for email in state.emails:
        if not email.read and email.category == "urgent":
            bonus -= 2.0
        if not email.ignored and email.category == "spam":
            bonus -= 0.2

    # Penalty for unresolved conflicts
    for meeting in state.meetings:
        if meeting.conflict and meeting.scheduled:
            bonus -= 1.0

    return bonus
