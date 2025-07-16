import requests
import json

scoring_uri = "http://<your-endpoint-dns>.eastus.azurecontainer.io/score"

headers = {
    "Content-Type": "application/json"
}

payload = {
    "messages": [
        {"role": "user", "content": "What does a cardiologist do?"}
    ]
}

response = requests.post(scoring_uri, headers=headers, data=json.dumps(payload))

print("Status Code:", response.status_code)
print("Response:", response.json())
