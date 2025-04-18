from setuptools import setup, find_packages
import os

# 读取README文件
readme_path = 'README.md'
long_description = (
    open(readme_path, encoding='utf-8').read()
    if os.path.exists(readme_path)
    else "配置文件处理和转换工具包"
)

setup(
    name="configkit",
    version="0.1.0",
    description="配置文件处理和转换工具包，支持YAML、TCL格式转换和字典合并",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="EDP Team",
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=[
        "pyyaml>=6.0.1",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    keywords="configuration, yaml, tcl, converter, dictionary, merge",
    project_urls={
        "Source": "https://github.com/yourusername/configkit",
    },
)