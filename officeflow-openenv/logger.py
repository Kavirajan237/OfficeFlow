import logging

logging.basicConfig(
    filename="officeflow.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def log_action(action, reward):
    logging.info(f"Action: {action}, Reward: {reward}")