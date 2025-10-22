from invoke import task
from dotenv import load_dotenv

load_dotenv()

@task
def setup(ctx):
    """Set up the development environment by installing dependencies."""
    ctx.run("uv python install 3.11.12", pty=True)
    ctx.run("uv sync", pty=True)

@task
def test(ctx):
    ctx.run("echo $TEST_ENV", pty=True)

@task
def setup_dvc(ctx):
    ctx.run("dvc init", pty=True)
    ctx.run("bash setup-dvc.sh", pty=True)

@task
def add_train_stage(ctx):
    ctx.run("dvc stage add -n train -d train.py -d data -o models/model.joblib -M metrics.csv python3 train.py", pty=True)    