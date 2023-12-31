from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT  = '-e .'
def get_requirements(filepath:str) -> List[str]:
    requirements = []

    with open(filepath,'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n',"") for req in requirements]
    

    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name="Cat_Dog_Classification",
    version='0.0.1',
    author = 'Ankit M Zanzmera',
    author_email="22msrds052@jainuniversity.ac.in",
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)