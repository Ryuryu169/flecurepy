import pkg_resources
import sys

__version__ = pkg_resources.get_distribution("flecure").version

if __name__ == "__main__":
    print("Installed flecure package")
