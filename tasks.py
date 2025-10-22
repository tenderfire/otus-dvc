from invoke import task

@task
def setup(ctx):
    """Set up the development environment by installing dependencies."""
    ctx.run("uv python install 3.11.12", pty=True)
    ctx.run("uv sync", pty=True)