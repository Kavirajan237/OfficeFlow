from env.office_env import OfficeEnv, Action

env = OfficeEnv()
obs = env.reset()

print("[START] task=office_task env=officeflow model=baseline-agent")

rewards = []
steps = 0
success = False

for step in range(1, 11):
    action = Action(action_type="read_email")
    observation, reward, done, info = env.step(action)
    rewards.append(reward)

    error = info.get("error", None)
    error_str = "null" if error is None else str(error)

    print(f"[STEP] step={step} action={action.action_type} reward={reward:.2f} done={str(done).lower()} error={error_str}")

    steps = step
    if done:
        success = True
        break

score = sum(rewards)
reward_str = ",".join([f"{r:.2f}" for r in rewards])

print(f"[END] success={str(success).lower()} steps={steps} score={score:.2f} rewards={reward_str}")