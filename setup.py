from setuptools import setup, find_packages

setup(
    name="earth-engine-stitcher",
    packages=find_packages(exclude=('tests*')),
    version='0.0.1'
)