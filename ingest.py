import os


def load_files(repo_path):

    texts = []

    allowed = [
        ".py",
        ".js",
        ".ts",
        ".java",
        ".cpp",
        ".md"
    ]

    for root, dirs, files in os.walk(repo_path):

        for file in files:

            if any(
                file.endswith(ext)
                for ext in allowed
            ):

                path = os.path.join(root, file)

                try:

                    with open(
                        path,
                        "r",
                        encoding="utf-8"
                    ) as f:

                        texts.append(
                            f.read()
                        )

                except Exception:
                    pass

    return texts


if __name__ == "__main__":

    files = load_files(
        "repositories/fastapi"
    )

    print(
        "Number of files loaded:",
        len(files)
    )

    if files:
        print("\nFirst 500 characters:\n")
        print(files[0][:500])