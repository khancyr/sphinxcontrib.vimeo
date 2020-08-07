#-*- coding:utf-8 -*-

import setuptools
from sphinxcontrib import vimeo


setuptools.setup(
    name='sphinxcontrib.vimeo',
    version=vimeo.__version__,
    packages=setuptools.find_packages(),
    install_requires=[
        'sphinx'
        ],
    author='James Douglass',
    license='3-Clause BSD',
    url='https://bitbucket.org/jdouglass/sphinxcontrib.vimeo',
    description='''embedding vimeo videos into sphinx''',
    long_description=vimeo.__doc__,
    namespace_packages=['sphinxcontrib'],
    classifiers=(
        'Programming Language :: Python'
        'Development Status :: 4 - Beta'
        'License :: OSI Approved :: BSD License'
        'Programming Language :: Python :: 2'
        'Programming Language :: Python :: 2.6'
        'Programming Language :: Python :: 2.7'
        'Programming Language :: Python :: 3'
        'Programming Language :: Python :: 3.3'
        'Topic :: Software Development :: Documentation')
)
