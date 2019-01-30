import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gstandaard",
    version="0.0.1",
    author="Mark Santcroos",
    author_email="m.a.santcroos@lumc.nl",
    description="Python package for working with the G-Standaard from Z-Index.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://git.lumc.nl/pongs/gstandaard-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
