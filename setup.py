from setuptools import setup, find_packages

setup(
    name="oxaudit",
    version='0.4.0',
    packages=find_packages(),
    install_requires=[
        "requests",  # To send HTTP requests to the FastAPI server
    ],
    entry_points={
        'console_scripts': [
            'oxaudit=oxaudit.cli:main',  # Command to run the CLI
        ],
    },
    description="A Python package to scan Solidity contracts using Oxaudit",
    author="OXAUDIT",
    author_email="oxaudit.eth@example.com",
    url="https://github.com/OXAUDIT/OXAudit/tree/main",  # Replace with your actual repo
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
