from azureml.core import Workspace
import os

def upload_data():
    ws = Workspace.from_config()
    datastore = ws.get_default_datastore()

    datastore.upload_files(
        files=["prepared_data.jsonl"],
        target_path="openai_fine_tune_data/",
        overwrite=True,
    )
    print("Data uploaded to Azure ML datastore.")

if __name__ == "__main__":
    upload_data()
