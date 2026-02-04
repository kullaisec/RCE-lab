from executor import run_system_command

def sanitize_input(data):
    return data.replace(";", "")

def log_and_execute(command):
    print(f"[LOG] Executing: {command}")
    return run_system_command(command)
