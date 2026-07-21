from setuptools import setup, find_packages

Repo_Name = "MLOps-Car-Price-Prediction-System"
SRC_Project = "Car_Price_Prediction_System"
Author_Name = "ROHAN-MAGADUM-DEV"
Author_Email = "rohanmagadum2004@outlook.com"

__version__ = "0.1.0"

setup(
    version=__version__,
    name=SRC_Project,
    author=Author_Name,
    author_email=Author_Email,
    package_dir={"": "src"},
    packages=find_packages(where="src")
)