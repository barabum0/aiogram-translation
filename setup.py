from setuptools import setup, find_packages

VERSION = '1'
DESCRIPTION = 'Simple translation addon for AIOGram'
LONG_DESCRIPTION = 'This python package is a translation addon for AIOGram v3'

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="aiogram_translation",
    version=VERSION,
    author="sushka",
    author_email="barabum@duck.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[
        'aiogram>=3.0.0b7',
        'pydantic'
    ],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'

    keywords=['python', 'aiogram', 'translation'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)