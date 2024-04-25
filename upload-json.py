import requests
import os

# Retrieve the API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("API key is not set in environment variables")

# Setup headers with the authorization token
headers = {
    'Authorization': f'Bearer {api_key}',
}

# Function to upload a file with a specified purpose
def upload_file(file_path, purpose):
    url = "https://api.openai.com/v1/files"
    files = {'file': open(file_path, 'rb')}
    data = {'purpose': purpose}

    response = requests.post(url, headers=headers, files=files, data=data)
    
    if response.status_code == 200:
        file_data = response.json()
        file_id = file_data['id']
        print(f"File uploaded successfully. File ID: {file_id}")
        return file_id
    else:
        print(f"Failed to upload file: {response.status_code} - {response.text}")
        return None

# Specify the file path and purpose
file_path = "prompt.jsonl"
purpose = "batch"

# Upload the file and retrieve the file ID
file_id = upload_file(file_path, purpose)