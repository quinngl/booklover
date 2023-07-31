from setuptools import setup, find_packages


setup(
    name='booklover',
    version='1.0.0',
    url='https://github.com/quinngl/booklover',
    author='Quinn Glovier',
    author_email='qdg9xwb@virginia.edu',
    description='Booklover class and unit tests created for DS 5100',
    packages=find_packages(),    
    install_requires=['numpy >= 1.11.1', 'matplotlib >= 1.5.1', 'pandas'],
)