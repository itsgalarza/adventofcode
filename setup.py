import os

from setuptools import setup, find_packages


def get_version():
    curr_dir = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(curr_dir, 'version.txt')) as version_file:
        return version_file.read().strip()

setup(
    name='adventofcode-time',
    version=get_version(),
    url='git@github.com:itsgalarza/adventofcode.git',
    maintainer='Javier G',
    description='Repo for AdventOfCode',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    platforms='any',
    setup_requires=['pytest-runner'],
)