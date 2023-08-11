import requests
import json
# import pprint
import os

# cmd = 'wget'
if os.path.isfile("file.txt") == True:
    file = open("file.txt", "r")
    content = file.read()
    file.close()
    if content:
        file = open("file.txt", "w")
        file.write("")
    else:
        print("No data found in Text file")
else:
    print("Creating file")
    file = open("file.txt", "a")


print("Requesting...")

url = 'https://sdk-os-static.mihoyo.com/hk4e_global/mdk/launcher/api/resource'
headers = {'Accept': 'application/json'}
params = {
    "channel_id": "1",
    "key": "gcStgarh",
    "launcher_id": "10",
    "sub_channel_id": "0"
}

r = requests.get(url, params, headers=headers)

if r.status_code == 200:
    content = json.loads(r.text)
    for sys1 in content['data']['game']['latest']['segments']:
        with open('file.txt', 'a') as f:
            f.write(sys1['path'])
            f.write("\n")
            print(sys1['path'])
else:
    print(f"Error: {r.status_code}")
