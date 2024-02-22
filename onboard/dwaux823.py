import requests
import uuid
bot_id = str(uuid.uuid4())
url = 'http://localhost:5000/register'
payload = {'id': bot_id}

response = requests.post(url, json=payload)

if response.status_code == 200:
    print(f"Bot with ID '{bot_id}' registered successfully.")
elif response.status_code == 400:
    print("Error: Missing bot ID in the request.")
else:
    print(
        f"Error: Failed to register bot. Status code: {response.status_code}")
