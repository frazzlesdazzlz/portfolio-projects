import os
import sys
import hashlib
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("VT_API_KEY")

file_name = sys.argv[1]

with open(file_name, "rb") as f:
    file_content = f.read()

file_hash = hashlib.sha256(file_content).hexdigest()

url = f"https://www.virustotal.com/api/v3/files/{file_hash}"

headers = {
    "x-apikey": api_key
}

response = requests.get(url, headers=headers)

if response.status_code == 404:
    print("VirusTotal has no record of this file hash.")
else:
    data = response.json()
    stats = data["data"]["attributes"]["last_analysis_stats"]
    print(f"Malicious: {stats['malicious']}")
    print(f"Suspicious: {stats['suspicious']}")
    print(f"Undetected: {stats['undetected']}")
    print(f"Harmless: {stats['harmless']}")