from utils import sanitize_input, log_and_execute

def handle_action(user_cmd):
    cleaned = sanitize_input(user_cmd)
    return log_and_execute(cleaned)

def handle_admin(task):
    return log_and_execute(task)
