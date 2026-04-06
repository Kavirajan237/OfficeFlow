# OfficeFlow OpenEnv

An OpenEnv environment that simulates an office workflow. An AI agent manages emails, calendar meetings, and tasks with deadlines over a limited number of steps per episode.

## Project Structure

```
officeflow/
├── env/
│   ├── __init__.py
│   ├── office_env.py   # OfficeEnv with step(), reset(), state()
│   ├── models.py       # Pydantic models: Action, Observation, Reward, OfficeState
│   ├── tasks.py        # Initial episode data (emails, meetings, tasks)
│   └── graders.py      # Reward logic and final scoring
├── inference.py        # Rule-based agent demo (replace with LLM agent)
├── openenv.yaml        # Environment spec
├── requirements.txt
├── Dockerfile
└── README.md
```

## Environment

### Actions

| Action | Description |
|---|---|
| `read_email` | Mark an email as read |
| `classify_email` | Set email category (urgent/normal/spam/meeting_request) |
| `reply_email` | Reply to an email |
| `schedule_meeting` | Schedule a meeting (detects conflicts) |
| `resolve_conflict` | Unschedule a conflicting meeting |
| `add_task` | Add a new task |
| `complete_task` | Mark a task as completed |
| `ignore_email` | Ignore/dismiss an email |

### Reward Signal

- Correct email classification: `+0.5`
- Reply urgent email: `+1.0`
- Ignore spam: `+0.5`
- Complete high-priority task: `+1.5`
- Resolve meeting conflict: `+0.8`
- Ignore urgent email: `-1.0`
- Reply spam: `-0.5`
- Schedule conflicting meeting: `-0.3`
- End-of-episode bonuses/penalties applied on top

## Run Locally

```bash
pip install -r requirements.txt
python inference.py
```

## Run with Docker

```bash
docker build -t officeflow .
docker run --rm officeflow
```

## Extending with an LLM Agent

Replace the `rule_based_policy` function in `inference.py` with an LLM call:

```python
def llm_policy(obs: Observation) -> Action:
    prompt = build_prompt(obs)          # serialize state to text
    response = call_your_llm(prompt)    # call OpenAI / Anthropic / etc.
    return parse_action(response)       # parse JSON → Action model
```
