from setuptools import setup, find_packages

setup(
    name='utils', 
    version='1.0.0',
    description='Utility functions for Flask app',
    author='Disha Modi',
    author_email='dishamodi3105@gmail.com',
    url='https://github.com/dishamodi0910/IdentifyTrue',  
    packages=find_packages(), 
    install_requires=[], 
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6', 
)
