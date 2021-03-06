import os

from setuptools import setup, find_packages


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()


setup(
    name='airavata-python-sdk',
    version='1.0.0',
    packages=find_packages(),
    package_data={'transport': ['*.ini'], 'sample': ['*.pem']},
    url='http://airavata.com',
    license='Apache License 2.0',
    author='Airavata Developers',
    author_email='dev@airavata.apache.org',
    description='Apache Airavata Python  SDK'
)
