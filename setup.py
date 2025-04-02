from setuptools import setup, find_packages
from typing import List

Hypen_e_dot='-e .'

def get_requirements(file_path:str)->List[str]:
    """
    This function returns a list of requirements from the requirements file.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]
        if Hypen_e_dot in requirements:
            requirements.remove(Hypen_e_dot)
    return requirements

setup(
    name="mlproject",
    version="0.1",
    author="Vijayakumar",
    author_email="vijayahiremath9@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)