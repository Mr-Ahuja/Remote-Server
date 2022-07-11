from fastapi import FastAPI
from pydantic import BaseModel

class Command(BaseModel):
    command: str

app = FastAPI()


@app.get("/")
def read_root():
    return {"200": "Welcome To Heroku"}


@app.post("/command/{session_id}")
async def read_item(item_id: int, command: Command | None):
    return {"item_id": item_id, "command": command}