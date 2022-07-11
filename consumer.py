import requests
from setuptools import Command

import random
import time

session_id = random.randint(0,100)
print("Your Session Id is : " + str(session_id))
while True:

    command = input("$ : ")
    r = requests.post("https://remote-terminal-mrahuja.herokuapp.com/command/"+str(session_id), json = {"command":str(command)})

    while True:
        r = requests.get("https://remote-terminal-mrahuja.herokuapp.com/command/"+str(session_id))
        response_data = r.json()
        if response_data["output"] != "":
            print(response_data["output"])
            break
        time.sleep(2)
