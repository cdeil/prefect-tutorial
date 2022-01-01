"""Prefect Orion hello world example.

From https://orion-docs.prefect.io/
"""
from prefect import flow, task
from typing import List
import httpx


@task(retries=3)
def get_stars(repo: str):
    url = f"https://api.github.com/repos/{repo}"
    count = httpx.get(url).json()["stargazers_count"]
    print(f"{repo} has {count} stars!")


# Note: flow is now created by decorating a function with `@flow`
@flow(name="Github Stars")
def github_stars(repos: List[str]):
    # Note: normal Python code (a for loop) is now used in a flow
    for repo in repos:
        get_stars(repo)


# run the flow!
github_stars(["PrefectHQ/Prefect", "PrefectHQ/miter-design"])
