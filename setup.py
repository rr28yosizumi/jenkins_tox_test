#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md',encoding='UTF8') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md',encoding='UTF8') as history_file:
    history = history_file.read()

requirements = [ ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="jenkins_tox_test",
    author_email='rr28_yosizumi@hotmail.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="jenkins tox test",
    entry_points={
        'console_scripts': [
            'jenkins_tox_test=jenkins_tox_test.cli:main',
        ],
    },
    install_requires=requirements,
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='jenkins_tox_test',
    name='jenkins_tox_test',
    packages=find_packages(include=['jenkins_tox_test', 'jenkins_tox_test.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='',
    version='0.1.0',
    zip_safe=False,
)
