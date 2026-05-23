from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

latest_command = {
    "action": "idle",
    "text": None
}

class Command(BaseModel):
    action: str
    text: str | None = None

@app.get("/")
def home():
    return {"status": "Dengdeng bridge is alive"}

@app.post("/command")
def command(cmd: Command):
    global latest_command
    latest_command = {
        "action": cmd.action,
        "text": cmd.text
    }
    print("收到动作：", latest_command)
    return {
        "ok": True,
        "received_action": cmd.action,
        "received_text": cmd.text
    }

@app.get("/latest")
def latest():
    return latest_command
