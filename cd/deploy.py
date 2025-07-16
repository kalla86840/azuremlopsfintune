from azureml.core import Workspace, Environment, Model, InferenceConfig
from azureml.core.webservice import AciWebservice, Webservice

def deploy_model():
    ws = Workspace.from_config()

    env = Environment(name="openai-env")
    env.python.conda_dependencies = Environment.from_pip_requirements_file(
        "cd/requirements_cd.txt"
    ).python.conda_dependencies

    inference_config = InferenceConfig(
        entry_script="cd/score.py",
        environment=env
    )

    deployment_config = AciWebservice.deploy_configuration(cpu_cores=1, memory_gb=1)

    service = Model.deploy(
        workspace=ws,
        name="openai-finetune-endpoint",
        models=[],
        inference_config=inference_config,
        deployment_config=deployment_config,
        overwrite=True
    )

    service.wait_for_deployment(show_output=True)
    print(f"Endpoint state: {service.state}")
    print(f"Scoring URI: {service.scoring_uri}")

if __name__ == "__main__":
    deploy_model()
