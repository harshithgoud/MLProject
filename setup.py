from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = "-e ."
def get_requirements(file_path:str) -> List[str]:

    requirements = []
    try:
        with open(file_path) as filepath:
            requirements = filepath.readlines()
            requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    return requirements




setup(
    name = "MLProject",
    author = "harshithgoud",
    author_email = "harsith1998@gmail.com",
    version = "0.0.1",
    packages = find_packages(),
    install_requires = get_requirements("requirements.txt")

)