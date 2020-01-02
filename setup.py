#!/usr/bin/env python
from setuptools import setup


setup(
    name='hamster-bridge',
    description='let your hamster log your work to your favorite bugtracker',
    version='0.8.0',
    author='Lars Kreisz',
    author_email='lars.kreisz@gmail.com',
    license='MIT',
    url='https://github.com/kraiz/hamster-bridge',
    extras_require={
        'redmine': ['python-redmine'],
    },
    packages=['hamster_bridge', 'hamster_bridge.listeners'],
    entry_points={'console_scripts': ['hamster-bridge = hamster_bridge:main']},
    long_description=open('README.rst').read(),
    install_requires=[
        'configparser>=4.0.0',
        'jira>=0.41',
        'python-dateutil>=2.8.0',
    ]
)
