from setuptools import setup

setup(
    name='BookLoverPackage',
    version='1.0.0',
    long_description=open("README.md").read(),
    long_description_content_type='text',
    description='A simple package which allows us to create a Book Lover instance with limited functionality.',
    url='https://github.com/BardiaNikpour/BookLover__B_N',
    author='BardiaNikpour',
    author_email='ddb4tr@virginia.edu',
    license='MIT',
    install_requires=[
        'pandas>=1.0.0'
    ],
    python_requires='>=3.7',
    packages=['BookLover']
)