from flask import Flask, request
from handlers import handle_action, handle_admin
from utils import log_and_execute

app = Flask(__name__)

@app.route("/run")
def run():
    cmd = request.args.get("cmd")        
    return handle_action(cmd)

@app.route("/admin")
def admin():
    payload = request.headers.get("X-Admin-Task")  
    return handle_admin(payload)

@app.route("/debug")
def debug():
    debug_cmd = request.args.get("debug")  
    return log_and_execute(debug_cmd)     

if __name__ == "__main__":
    app.run()
