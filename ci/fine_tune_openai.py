import openai
import os
import json

def fine_tune():
    openai.api_key = os.environ.get("OPENAI_API_KEY")
    if not openai.api_key:
        raise EnvironmentError("Missing OPENAI_API_KEY")

    file_response = openai.File.create(
        file=open("prepared_data.jsonl", "rb"),
        purpose="fine-tune"
    )
    print(f"Uploaded file ID: {file_response['id']}")

    fine_tune_resp = openai.FineTuningJob.create(
        training_file=file_response["id"],
        model="gpt-3.5-turbo",
    )
    print(f"Fine-tune job started: {fine_tune_resp['id']}")

if __name__ == "__main__":
    fine_tune()
