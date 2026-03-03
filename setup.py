from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Hotel_Reservation_Pratical_Lab",
    version="0.1.0",
    author="EL Aouan Mohamed",
    packages=find_packages(),
    install_requires=requirements
)