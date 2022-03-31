from curses import longname
from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf-8') as f:
    long_desc = f.read()

setup(
    name="src",
    version="0.0.1",
    author="AveshVerma",
    description="A small package for DVC ML Pipeline",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    author_email="verma.avesh001@gmail.com",
    url="https://github.com/AveshVerma/simple-dvc-project",
    package_directory={"":"src"},
    packages=find_packages(where="src"),
    license="GNU",
    python_requires=">=3.6",
    install_requires=[
        'dvc',
        'dvc[gdrive]',
        'dvc[s3]',
        'pandas',
        'scikit-learn',
        
    ]
)