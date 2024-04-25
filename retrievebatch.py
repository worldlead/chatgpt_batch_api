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

def retrieve_batch(batch_id):
    
    url = "https://api.openai.com/v1/batches/" + batch_id 

    # Make the GET request
    response = requests.get(url, headers=headers)

    # Check the response
    if response.status_code == 200:
        batch_info = response.json()
        print("Batch retrieved successfully.")
        print(batch_info)
    else:
        print(f"Failed to retrieve batch: {response.status_code} - {response.text}")

batch_id = "batch_Qnyg4YZGIQO8i5MqeRIgM03l"
retrieve_batch(batch_id)