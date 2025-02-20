from setuptools import setup, find_packages

setup(
    name="medsy_schema",
    version="0.7.5",
    description="Schema for Flask Admin and User backends",
    author="wizzgeeks",
    author_email="",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    python_requires=">=3.7",
)
