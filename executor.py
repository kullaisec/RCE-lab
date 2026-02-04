import subprocess

def run_system_command(cmd):
    return subprocess.check_output(cmd, shell=True, text=True)
