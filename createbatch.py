import requests
import os

# Get the API key from an environment variable
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("API key is not set in environment variables")

# Set up the headers
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

# Define the URL for the batch creation endpoint
url = "https://api.openai.com/v1/batches"

# Data for creating the batch
data = {
    "input_file_id": "file-paQjtNh7HvtGJK7EKRBD1Z6H",  # Use your actual file ID
    "endpoint": "/v1/chat/completions",
    "completion_window": "24h",
    "metadata": {
        "max_tokens": "1424",
        "temperature": "0.7"
    }
}

# Make the POST request
response = requests.post(url, headers=headers, json=data)

# Check the response
if response.status_code == 200:
    batch_info = response.json()
    print("Batch created successfully.")
    print("Batch ID:", batch_info['id'])
    print(batch_info)
else:
    print(f"Failed to create batch: {response.status_code} - {response.text}")