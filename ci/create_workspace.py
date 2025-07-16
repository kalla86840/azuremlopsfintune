from azureml.core import Workspace
import json

def create_workspace():
    with open("ci/config.json") as f:
        config = json.load(f)

    ws = Workspace.create(
        name=config["workspace_name"],
        subscription_id=config["subscription_id"],
        resource_group=config["resource_group"],
        location=config["location"],
        exist_ok=True,
        show_output=True
    )
    ws.write_config(path=".")
    print("Workspace created and config written.")

if __name__ == "__main__":
    create_workspace()
