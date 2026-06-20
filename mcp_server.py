import os


def list_files():

    return os.listdir(
        "repositories"
    )


def read_file(path):

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as f:

        return f.read()


if __name__ == "__main__":

    print("Repositories:")
    print(list_files())

    print("\nFirst 500 characters:\n")

    file_path = (
        "repositories/fastapi/README.md"
    )

    print(
        read_file(file_path)[:500]
    )