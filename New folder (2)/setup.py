from setuptools import setup, find_packages

setup(
    name="oxaudit",                     
    version="0.1",                      
    packages=find_packages(),           
    install_requires=[],                
    description="A simple package with a function that prints 'Hello, world!'",
    long_description=open("README.md").read(),    
    long_description_content_type="text/markdown", 
    url="https://github.com/OXAUDIT/OXAudit",  
    author="Your Name",                 
    author_email="you@example.com",     
    license="MIT",                      
    classifiers=[                       
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",            
    entry_points={
        'console_scripts': [
            'oxaudit=oxaudit.cli:main',  # Entry point for the command
        ],
    },
)
