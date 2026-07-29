import os
import requests

from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("VT_API_KEY")

url = "https://www.virustotal.com/api/v3/users/frazzlesdazzles"

headers = {
    "x-apikey": api_key
}

response = requests.get(url, headers=headers)

print(response.status_code)

data = response.json()

print(data["data"]["id"])
print(data["data"]["attributes"]["first_name"])
print(data["data"]["attributes"]["last_name"])
print(data["data"]["attributes"]["user_since"])

print(data["data"]["attributes"]["private"])