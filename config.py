import os

OUTPUT = f"{os.getcwd()}/output"


def create_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)
