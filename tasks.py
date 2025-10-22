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