from setuptools import setup, find_packages

setup(
    name='flecurepy',
    version="0.1.0",
    description="Package for flecure",
    author='Kaname',
    packages=find_packages(),
    license='MIT',
    install_requires=["requests", "PyCryptodome"],
)