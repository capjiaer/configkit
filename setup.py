from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="configkit",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Configuration format conversion toolkit for YAML and TCL",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/configkit",
    packages=find_packages(),
    install_requires=[
        "PyYAML>=5.1",
    ],
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    keywords="yaml tcl configuration converter",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/configkit/issues",
        "Source": "https://github.com/yourusername/configkit",
    },
)