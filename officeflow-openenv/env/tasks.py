from datetime import datetime, timedelta
from env.models import Email, Meeting, Task

NOW = datetime(2026, 4, 6, 9, 0, 0)


def get_initial_emails():
    return [
        Email(
            id="e1",
            sender="ceo@company.com",
            subject="URGENT: Board presentation tomorrow",
            body="We need the Q1 report ready by 8am tomorrow. Please confirm.",
            category="urgent",
        ),
        Email(
            id="e2",
            sender="newsletter@promo.com",
            subject="50% off office supplies!",
            body="Click here for amazing deals on pens, paper, and more!",
            category="spam",
        ),
        Email(
            id="e3",
            sender="hr@company.com",
            subject="Team lunch this Friday",
            body="We're organizing a team lunch on Friday at noon. Please RSVP.",
            category="normal",
        ),
        Email(
            id="e4",
            sender="client@bigcorp.com",
            subject="Meeting request: Project kickoff",
            body="Can we schedule a 1-hour kickoff meeting this week? I'm free Wed 2-4pm or Thu 10-12.",
            category="meeting_request",
        ),
        Email(
            id="e5",
            sender="dev@company.com",
            subject="Code review needed",
            body="PR #42 is ready for review. It fixes the login bug reported last week.",
            category="normal",
        ),
    ]


def get_initial_meetings():
    return [
        Meeting(
            id="m1",
            title="Weekly standup",
            start_time=NOW + timedelta(hours=1),
            end_time=NOW + timedelta(hours=1, minutes=30),
            attendees=["team@company.com"],
            scheduled=True,
        ),
        Meeting(
            id="m2",
            title="Project kickoff with BigCorp",
            start_time=NOW + timedelta(days=2, hours=2),
            end_time=NOW + timedelta(days=2, hours=3),
            attendees=["client@bigcorp.com"],
            scheduled=False,
        ),
        Meeting(
            id="m3",
            title="1:1 with manager",
            start_time=NOW + timedelta(hours=1),
            end_time=NOW + timedelta(hours=2),
            attendees=["manager@company.com"],
            scheduled=True,
            conflict=True,  # overlaps with m1
        ),
    ]


def get_initial_tasks():
    return [
        Task(
            id="t1",
            title="Prepare Q1 report",
            description="Compile Q1 financials and metrics for board presentation",
            deadline=NOW + timedelta(hours=23),
            priority="high",
        ),
        Task(
            id="t2",
            title="Review PR #42",
            description="Review and approve the login bug fix pull request",
            deadline=NOW + timedelta(days=1),
            priority="medium",
        ),
        Task(
            id="t3",
            title="Update project roadmap",
            description="Update the roadmap doc with Q2 milestones",
            deadline=NOW + timedelta(days=3),
            priority="low",
        ),
    ]
