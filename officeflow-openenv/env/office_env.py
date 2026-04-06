from typing import Dict, Any
from pydantic import BaseModel
import random
from database import init_db
from logger import log_action

class Action(BaseModel):
    action_type: str

class OfficeEnv:
    def __init__(self):
        self.max_steps = 20
        init_db()
        self.reset()

    def reset(self):
        self.current_step = 0
        self.score = 0
        self.tasks_completed = 0

        # Generate random emails
        email_types = ["boss", "client", "team", "spam", "meeting"]
        priorities = ["high", "medium", "low"]

        self.emails = []
        for i in range(5):
            self.emails.append({
                "type": random.choice(email_types),
                "priority": random.choice(priorities),
                "handled": False
            })

        # Tasks with deadlines
        self.tasks = [
            {"task": "Prepare Report", "deadline": 5, "completed": False},
            {"task": "Client Presentation", "deadline": 8, "completed": False},
            {"task": "Code Review", "deadline": 6, "completed": False}
        ]

        return self.state()

    def state(self) -> Dict[str, Any]:
        return {
            "step": self.current_step,
            "score": self.score,
            "tasks_completed": self.tasks_completed,
            "emails": self.emails,
            "tasks": self.tasks
        }

    def step(self, action: Action):
        reward = 0
        done = False
        info = {}

        if action.action_type == "read_email":
            reward = 0.1

        elif action.action_type == "classify_email":
            reward = 0.2

        elif action.action_type == "reply_email":
            reward = 0.3
            self.tasks_completed += 1

        elif action.action_type == "schedule_meeting":
            reward = 0.4
            self.tasks_completed += 1

        elif action.action_type == "complete_task":
            reward = 0.5
            self.tasks_completed += 1

        else:
            reward = -0.1
            info["error"] = "Invalid action"

        self.score += reward
        log_action(action.action_type, reward)

        self.current_step += 1
        if self.current_step >= self.max_steps:
            done = True

        return self.state(), reward, done, info