from git import Repo
import os

def clone_repo(repo_url):

    repo_name = repo_url.split("/")[-1]

    repo_path = os.path.join(
        "repositories",
        repo_name
    )

    if not os.path.exists(repo_path):
        Repo.clone_from(
            repo_url,
            repo_path
        )

    return repo_path


if __name__ == "__main__":

    path = clone_repo(
        "https://github.com/tiangolo/fastapi"
    )

    print(path)