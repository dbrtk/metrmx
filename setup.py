import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


install_requires = []
with open('requirements.txt', 'r') as _file:
    for package in _file.readlines():
        package = package.strip()
        if package:
            install_requires.append(package)


setup(
    name="metrmx",
    version="0.0.1",
    author="Dominik Bartkowski",
    author_email="dominik.bartkowski@gmail.com",
    description="Metrics for rmx services running on rabbitmq.",
    license="BSD",
    keywords="metrics, rabbitmq",
    url="http://dbrtk.org",
    packages=['metrmx', 'tests'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",

        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',

        'Natural Language :: English',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',

        'Operating System :: POSIX :: Linux',
        'Operating System :: Unix',

    ],
    install_requires=install_requires,
)
