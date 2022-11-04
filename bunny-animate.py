import requests
import os
import time

owner = "diracdeltas"
repo = "tweets"
ref = "f7d8522ece59f97c49f53784b83ddbfb69c83c35"
url = "https://api.github.com"

bunny_commit = requests.get(f"{url}/repos/{owner}/{repo}/commits/{ref}")

frames = bunny_commit.json().get("commit").get("message").split("\n\n")
print(len(frames))

while True:
    for i in range(1, 23):
        os.system('clear')
        print(frames[i])
        time.sleep(0.25)
