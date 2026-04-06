from pydantic import BaseModel, Field
from typing import Optional, List, Literal
from datetime import datetime


class Email(BaseModel):
    id: str
    sender: str
    subject: str
    body: str
    category: Literal["urgent", "normal", "spam", "meeting_request"] = "normal"
    read: bool = False
    replied: bool = False
    ignored: bool = False


class Meeting(BaseModel):
    id: str
    title: str
    start_time: datetime
    end_time: datetime
    attendees: List[str] = []
    scheduled: bool = False
    conflict: bool = False


class Task(BaseModel):
    id: str
    title: str
    description: str
    deadline: datetime
    priority: Literal["low", "medium", "high"] = "medium"
    completed: bool = False
    overdue: bool = False


class OfficeState(BaseModel):
    emails: List[Email] = []
    meetings: List[Meeting] = []
    tasks: List[Task] = []
    current_step: int = 0
    max_steps: int = 20
    score: float = 0.0
    done: bool = False


class Action(BaseModel):
    action_type: Literal[
        "read_email",
        "classify_email",
        "reply_email",
        "schedule_meeting",
        "resolve_conflict",
        "add_task",
        "complete_task",
        "ignore_email",
    ]
    target_id: Optional[str] = None
    classification: Optional[Literal["urgent", "normal", "spam", "meeting_request"]] = None
    reply_body: Optional[str] = None
    task_title: Optional[str] = None
    task_description: Optional[str] = None
    task_deadline: Optional[datetime] = None
    task_priority: Optional[Literal["low", "medium", "high"]] = None


class Observation(BaseModel):
    state: OfficeState
    last_action_result: str = ""
    available_actions: List[str] = []


class Reward(BaseModel):
    value: float
    reason: str
    cumulative: float
