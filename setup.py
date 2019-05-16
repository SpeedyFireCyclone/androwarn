import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'requirements.txt'), 'r') as f:
    requirements = f.readlines()

setup(
    name='androwarn',
    version='1.5-1',
    description='Androwarn, Yet another static code analyzer for malicious Android applications',
    long_description='''Androwarn is a tool whose main aim is to detect and warn the user about potential malicious behaviours developped by an Android application.
The detection is performed with the static analysis of the application's Dalvik bytecode, represented as Smali, with the androguard library.
This analysis leads to the generation of a report, according to a technical detail level chosen from the user.''',
    author='Thomas Debize',
    author_email='',
    url='https://github.com/maaaaz/androwarn',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'androwarn=bin.__main__:main'
        ]
    }
)
