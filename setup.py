from setuptools import setup, find_packages
from os import path
import re

def read(*relpath):
    with open(path.join(path.dirname(__file__), *relpath)) as fp:
        return fp.read()

def get_version(*relpath):
    match = re.search(
        r'''^__version__ = ['']([^'']*)['']''',
        read(*relpath),
        re.M
    )
    if not match:
        raise RuntimeError('Unable to find version string.')
    return match.group(1)

setup(
    name='croatian_stemmer',
    version=get_version('croatian_stemmer.py'),
    description='A stemmer for Croatian language',
    long_description=read('README.md'),
    url='https://bitbucket.org/luismsgomes/toolwrapper',
    author='Luís Gomes',
    author_email='luismsgomes@gmail.com',
    license='GNU General Public License v3 (GPLv3)',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Linguistic',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='stemmer croatian',
    py_modules=['croatian_stemmer'],
    packages=['croatian_stemmer'],
    package_dir={'croatian_stemmer': 'croatian_stemmer'},
    package_data={'croatian_stemmer': ['rules.txt', 'transformations.txt']},
    entry_points={
        "console_scripts": [
            "croatian_stemmer=croatian_stemmer:main",
        ],
    },
)
