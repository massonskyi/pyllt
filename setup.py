from setuptools import setup, find_packages

setup(
    name='pyllt',
    version='0.1.0',
    author='mssnskyi',
    author_email='_',
    description='low and high level tools API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/massonskyi/pyllt',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',
    install_requires=[
        'setuptools',
    ],
    entry_points={
        'console_scripts': [

        ],
    },
)
