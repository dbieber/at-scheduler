from setuptools import find_packages
from setuptools import setup

scripts = [
    'bin/at',
]

dependencies = [
    'APScheduler>=3.0.0',
    'parsedatetime>=1.5',
    'python-daemon>=2.0.0',
    'redis>=2.0.0',
]

setup(
    name='at-scheduler',
    version='0.0',
    license='Apache 2.0',
    url='http://davidbieber.com/at-scheduler',
    author='David Bieber',
    author_email='david810@gmail.com',
    description='at, the simple command line scheduler',
    packages=find_packages(),
    include_package_data=True,
    scripts=scripts,
    install_requires=dependencies,
)
