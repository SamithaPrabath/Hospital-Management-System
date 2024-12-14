
from setuptools import setup, find_packages

setup(
    name='async-mysql-library',
    version='1.0.0',
    description='An asynchronous MySQL library using aiomysql',
    packages=find_packages(),
    install_requires=[
        'aiomysql',
    ],
    python_requires='>=3.6',  # Specify the supported Python versions
    author='Samitha Prabath',
    author_email='samithaprabath513@gmail',
    # url='https://github.com/yourusername/async-mysql-library',
)
