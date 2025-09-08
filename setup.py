from setuptools import setup, find_packages

# Read the long description from README.md
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read install requirements from requirements.txt
with open("requirements.txt") as f:
    install_requires = f.read().splitlines()

setup(
    name="weather_cli",
    version="0.0.1",
    author="Ishan Bhat",
    author_email="ishan2003bhat@gmail.com",
    description="A Python CLI tool to fetch live weather data using OpenWeather API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=install_requires,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "weather=weather_cli.cli:main",
        ],
    },
    keywords="weather cli python-cli",
    include_package_data=True,
)
