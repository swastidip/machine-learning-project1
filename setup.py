from setuptools import setup
from typing import List

#Declaring variables for setup function



PROJECT_NAME="housing-predictor"
VERSION="0.0.1"
AUTHOR="Swastidip"
DESCRIPTION="This is a  machine learnig project on regression"
PACKAGES=["housing"]
REQUIREMENTS_FILE_NAME="requirements.txt"


def get_requirements_list()->List[str]:
    """
      Description:this function returns requirements mentioned in requirements.txt file
      
      return This function is going to return a list which contain name of library mentioned
      in requirements.txt

      """
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        requirement_file.readlines() 
    


setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=PACKAGES,
install_requires=get_requirements_list()


    )



