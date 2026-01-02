from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

REPO_NAME = "ML Based Books Recommender System"
AUTHOR_USER_NAME = "SENESH HANSANA"
SRC_REPO = "Books-Recommender-Engine"
LIST_OF_REQUIREMENTS = []


setup(
    name=SRC_REPO,
    version="0.0.1",
    author="SENESH HANSANA",
    description="A small local packages for ML based books recommendations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/seneshMH/Books-Recommender-Engine",
    author_email="senesh.m.hansana@gmail.com",
    packages=find_packages(),
    license="MIT",
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
)