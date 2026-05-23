from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Command(BaseModel):
    action: str
    text: str | None = None

@app.get("/")
def home():
    return {"status": "Adeng bridge is alive"}

@app.post("/command")
def command(cmd: Command):
    print("收到动作：", cmd.action, "文字：", cmd.text)
    return {
        "ok": True,
        "received_action": cmd.action,
        "received_text": cmd.text
    }
