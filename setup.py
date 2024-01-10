from setuptools import setup, find_packages

setup(
    name='flecurepy',
    version="0.0.2",
    description="package for flecure",
    author='kaname',
    # package_dir={'': 'src'},
    packages=find_packages(),
    license='MIT',
    install_requires=["flask"],
)