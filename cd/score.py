import json
import openai

openai.api_key = "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"

FINE_TUNED_MODEL = "ft:gpt-3.5-turbo:your-org::abc123"

def init():
    pass

def run(raw_data):
    try:
        payload = json.loads(raw_data)
        response = openai.ChatCompletion.create(
            model=FINE_TUNED_MODEL,
            messages=payload["messages"]
        )
        return {"response": response["choices"][0]["message"]["content"]}
    except Exception as e:
        return {"error": str(e)}
