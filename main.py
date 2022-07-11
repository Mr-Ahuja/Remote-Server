from fastapi import FastAPI
from pydantic import BaseModel
import os
from os.path import exists
import json

class Command(BaseModel):
    command: str

class CommandOutput(BaseModel):
    command_output: str

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome To Remote Terminal"}


@app.post("/command/{session_id}")
async def send_command(session_id: int, command: Command):
    if not exists("sessions"):
        os.makedirs("sessions")
    if exists("sessions/" + str(session_id)):
        return { "message" : "Command Execution in Process" }

    json_output = {
        "command" : command.command,
        "output" : ""
    }
    with open("sessions/" + str(session_id) + ".json", 'w') as command_file:
        command_file.write(json.dumps(json_output, indent = 4))

    return {"item_id": session_id, "command": command}


@app.get("/command/{session_id}")
async def request_command_response(session_id: int):
    if exists("sessions/" + str(session_id) + ".json"):
        command_file = open("sessions/" + str(session_id) + ".json", "r")
        return { "output" : command_file.readlines() }
    return { "output" : "" }

@app.post("/command_response/{session_id}")
async def request_command_response(session_id: int,command_output : CommandOutput):
    json_output = {}
    with open("sessions/" + str(session_id) + ".json", 'r') as command_file:
        json_output = json.load(command_file)
    with open("sessions/" + str(session_id) + ".json", 'w') as command_file:
        json_output["output"] = command_output.command_output
        command_file.write(json.dumps(json_output, indent = 4))

    return { "message" : "Done" }