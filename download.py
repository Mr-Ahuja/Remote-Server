import requests
import sys

url = 'https://remote-terminal-mrahuja.herokuapp.com/download/' + str(sys.argv[1])
r = requests.get(url, allow_redirects=True)

open(str(sys.argv[1]), 'wb').write(r.content)