import requests

# Make a request call to the API
url = 'https://sdk-os-static.mihoyo.com/hk4e_global/mdk/launcher/api/resource'
headers = {'Accept': 'application/json'}
params = {
    "channel_id": "1",
    "key": "gcStgarh",
    "launcher_id": "10",
    "sub_channel_id": "0"
}

r = requests.get(url, params, headers=headers)

converted_json = r.json()

# Get the latest version in the API
latest_version = converted_json['data']['game']['latest']['version']

# Save the latest version to a text file
with open('version.txt', 'w') as f:
    f.write(latest_version)
    f.close()

# Get the latest version from the text file
with open('version.txt', 'r') as f:
    latest_version = f.read()
    f.close()

# Get the current version from the text file
with open('current_version.txt', 'r') as f:
    current_version = f.read()
    f.close()

# Compare the latest version to the current version
if latest_version == current_version:
    print('No updates needed')
else:
    print('Updates needed')
    print(f'Latest version: {latest_version}')
    print(f'Current version: {current_version}')
    # Do something here to update the game
    # Save the latest version to the current version text file
    with open('current_version.txt', 'w') as f:
        f.write(latest_version)
        f.close()