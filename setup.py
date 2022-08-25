from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in xpert/__init__.py
from xpert import __version__ as version

setup(
	name="xpert",
	version=version,
	description="Xpert customizations",
	author="V",
	author_email="moustafa.imym@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
