"""Packaging settings."""

from codecs import open
from os.path import abspath, dirname, join
from subprocess import call

from setuptools import Command, find_packages, setup

from lykke import __version__

this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.rst'), encoding='utf-8') as file:
    long_description = file.read()


class RunTests(Command):
    """Run all tests."""
    description = 'run tests'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        """Run all tests!"""
        errno = call(['py.test'])
        raise SystemExit(errno)


setup(
    name='lykke',
    version=__version__,
    description='Lykke exchange command line tool',
    long_description=long_description,
    url='https://github.com/pfeffer90/lykke',
    author='Paul Pfeiffer',
    author_email='pfeifferpaul90@gmail.com',
    license='UNLICENSE',
    keywords='cli',
    packages=find_packages(exclude=['docs', 'tests*']),
    install_requires=['docopt'],
    tests_require=['coverage', 'pytest', 'pytest-cov'],
    entry_points={
        'console_scripts': [
            'lykkex=lykke.cli:main',
        ],
    },
    cmdclass={'test': RunTests},
)
