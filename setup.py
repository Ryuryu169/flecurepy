from setuptools import setup, find_packages

setup(
    name='flecure',
    version="0.0.1",
    description="package for flecure",
    author='kaname',
    package_dir={'': ''},
    packages=find_packages(),
    license='MIT',
    install_requires=["flask"],
)