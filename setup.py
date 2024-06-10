from setuptools import setup, find_packages
from Cython.Build import cythonize
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
    ext_modules=cythonize(
        [
         'pyllt/converter/to_bytearray.py',
         'pyllt/functiontools/searchs/binary.py',
         'pyllt/functiontools/searchs/linear.py',
         'pyllt/functiontools/searchs/ternary.py',
         'pyllt/functiontools/pretty_print.py',
         'pyllt/pyllt/command.py',
         'pyllt/pyllt/factory.py',
         'pyllt/pyllt/functor.py',
         'pyllt/pyllt/mediator.py',
         'pyllt/pyllt/meta.py',
         'pyllt/pyllt/observer.py',
         'pyllt/pyllt/singleton.py',
         'pyllt/pyllt/smart_ptr.py',
         'pyllt/pyllt/time_ptr.py',
         'pyllt/pyllt/visitor.py',
         'pyllt/pyhlt/acd.py',
         'pyllt/pyhlt/cache.py',
         'pyllt/pyhlt/class_method_checked.py',
         'pyllt/pyhlt/context_manager.py',
         'pyllt/pyhlt/log_calls.py',
         'pyllt/pyhlt/memoization.py',
         'pyllt/pyhlt/retry.py',
         'pyllt/pyhlt/singleton.py',
         'pyllt/pyhlt/timeit.py',
         'pyllt/pyhlt/type.py',
         ],
        language_level='3',  # Используйте языковой уровень Python 3
    ),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',
    install_requires=[
        'setuptools',
        'numpy',
    ],
    entry_points={
        'console_scripts': [

        ],
    },
)
