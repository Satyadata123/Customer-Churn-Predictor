from setuptools import find_packages, setup
from typing import List

Hypen = '-e .'
def get_requirement(file: str) -> List[str]:
    requirement =  []
    with open(file) as file_obj:
        requirement = file_obj.readline()
        requirement = [req.replace("\n", "") for req in requirement]
        if Hypen in requirement:
            requirement.remove(Hypen)


    return requirement


setup(
    name="Churn_predetion",
    author="Satyam singh",
    version="1.0.0",
    author_email="satyamsinghsolanki2005@gmail.com",
    packages=find_packages(),
    install_requires= get_requirement(r"C:\Users\Admin\OneDrive\Desktop\churn_prediction\requirements.txt")
)