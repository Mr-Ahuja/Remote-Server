import requests
import sys

server = "https://remote-terminal-mrahuja.herokuapp.com"
url = server + '/upload'
file = {'file': open(sys.argv[0], 'rb')}
resp = requests.post(url=url, files=file) 
print(resp.json())