# VirusTotal File Hash Checker

A Python command-line tool that calculates the SHA-256 hash of a file and checks that hash against the VirusTotal API.

## What It Does

- Accepts a file path as a command-line argument
- Opens the file in binary mode
- Generates its SHA-256 hash
- Sends the hash to the VirusTotal API
- Uses an API key stored securely in a `.env` file
- Extracts VirusTotal's latest analysis statistics
- Displays malicious, suspicious, undetected, and harmless results
- Handles hashes that VirusTotal does not recognise

## Requirements

- Python 3
- `requests`
- `python-dotenv`
- A VirusTotal API key

## Setup

Create a `.env` file inside the project folder:

```text
VT_API_KEY=your_api_key_here