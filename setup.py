# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='agespysawrapper',
    version='0.1.1',
    url='https://github.com/diegofsousa/agespysa',
    license='MIT License',
    author='Diego F Sousa',
    author_email='diegofernando5672@gmail.com',
    keywords='contas agua piaui portugues',
    description=u'API wrapper para buscar contas de água da AGESPISA - Piauí',
    packages=['agespysawrapper'],
    install_requires=['requests', 'bs4'],
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
)