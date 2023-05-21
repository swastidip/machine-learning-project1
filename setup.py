from setuptools import setup
from typing import List


#declaring variables for setup function

PROJECT_NAME="housing_predictror"
VERSION="0.0.1"
AUTHOR="swastidip sahoo"
DESCRIPTION="machine learning project"
PACKAGES=["housing"]
REQUIREMENTS_FILE_NAME="requirements.txt"



def get_requirements_list()->List[str]:
    """
    Description: This funcn is going to return list of requirements 
    mentioned in requiremnts.txt file

    return This function returns name of libraries mentioned in 
    requirements.txt

    """
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        return requirement_file.readline()








setup(

    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=PACKAGES,
    install_requires=get_requirements_list()
)
