import requests
import json
import os

if os.path.isfile("GI/GB/update_voice.txt") == True:
    file = open("GI/GB/update_voice.txt", "r")
    content = file.read()
    file.close()
    if content:
        print("Cleaning existing data")
        file = open("GI/GB/update_voice.txt", "w")
        file.write("")
    else:
        print("No data found in Text file")
else:
    print("Creating file")
    file = open("GI/GB/update_voice.txt", "a")


print("Getting Requested content")

url = 'https://sdk-os-static.mihoyo.com/hk4e_global/mdk/launcher/api/resource'
headers = {'Accept': 'application/json'}
params = {
    "channel_id": "1",
    "key": "gcStgarh",
    "launcher_id": "10",
    "sub_channel_id": "0"
}

r = requests.get(url, params, headers=headers)

# Add a check for status code

if r.status_code == 200:
    content = json.loads(r.text)
    for sys1 in content['data']['game']['diffs'][0]['voice_packs']:
        # Get URL Links from JSON dict ['data']['game']['latest']['segments']['path'] and write to text file with numbers on each line
        file = open("GI/GB/update_voice.txt", "a")
        file.write(sys1['path'] + "\n")
        file.close()
else:
    print(f"Error: {r.status_code}")
