# This will be executed everytime we make a pip install
# The find_packages is very important since it's used to
# make all our packages visible to each other inside the project

from setuptools import setup, find_packages
setup(
    name='Winteam Bridge',
    version='1.0.0',
    description='Brosnan\'s winteam bridge',
    packages=find_packages(exclude=['*tests']),
    include_package_data=True,
    setup_requires=[
        'pytest-runner',
    ],
    test_suite='test.unittest'
)
