#!/usr/bin/python3
# Copyright 2023 BISITE
# See LICENSE for details.
# Author: Francisco Pinto-Santos (@GandalFran on GitHub)


import io

from setuptools import find_packages, setup


def readme():
    with io.open('README.md', encoding='utf-8') as f:
        return f.read()


def requirements(filename):
    with io.open(filename, encoding='utf-8') as f:
        for line in f.readlines():
            yield line.strip()


setup(
    name='panelais_models_api',
    version='2.0',
    packages=find_packages(),
    url="https://github.com/iSkYrIsE/panelais-models-api-api",
    download_url='https://github.com/iSkYrIsE/panelais-models-api-api/archive/1.0.tar.gz',
    license='LICENSE.md',
    author='BISITE',
    author_email='marcgomezdequero99@gmail.com',
    description='',
    long_description=readme(),
    long_description_content_type='text/markdown',
    install_requires=list(requirements(filename='requirements.txt')),
    data_files=[],
    entry_points={
        'console_scripts': [
            'panelais_models_api=panelais_models_api.run:main'
        ],
    },
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Intended Audience :: Developers"
    ],
    python_requires='>=3',
    project_urls={
        'Bug Reports': 'https://github.com/iSkYrIsE/panelais-models-api-api/issues',
        'Source': 'https://github.com/iSkYrIsE/panelais-models-api-api'
    },
)
