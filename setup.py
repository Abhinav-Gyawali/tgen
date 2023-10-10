from setuptools import setup, find_packages
import os

VERSION = '0.0.1'
DESCRIPTION = 'Making token verification'
LONG_DESCRIPTION = 'A pacckage that allows you to generate a token for different purposes like to make , verify token.'

# Setting up
setup(
    name="tgen",
    version=VERSION,
    author="ABlI (Abhinav Gyawali)",
    author_email="<contact@abhinav-gyawali.com.np>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['six', 'django'],
    keywords=['python', 'token', 'generator', 'verifiaction', 'django'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Web Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)