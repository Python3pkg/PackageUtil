import subprocess
import os
from sys import version
from time import ctime
import shutil

class Package:
	def __init__(self, package_id=None, version=None, volume=None, location=None, install_time=None, groups=None):
		self.package_id = package_id
		self.version = version
		self.volume = volume
		self.location = location
		self.install_time = install_time
		self.groups = groups
		self._files = None


	def __repr__(self):
		return "%s | Version: %s | Volume: %s | Location: %s | Installed on: %s" % (self.package_id, self.version, self.volume, self.location, ctime(float(self.install_time)))


	@property
	def is_dead(self):
		for file in self.files:
			if not os.path.isdir(file):
				if os.path.isfile(file):
					return False
		return True


	@property
	def files(self):
		if self._files == None:
			files = []
			for file in subprocess.check_output(["pkgutil", "--only-files", "--files", self.package_id]).decode().split("\n")[:-1]:
				if not self.location:
					self.location = "/"
				if self.location == "/" and self.volume == "/":
					self.volume = ""
				files.append("%s%s%s" % (self.volume, self.location + "/" if self.location[-1] != "/" else self.location, file))
			self._files = files
		return self._files

	@property
	def common_prefix(self):
		return os.path.commonprefix(self.files).rpartition(os.path.sep)[0]


def get_installed_packages(include_apple_packages=False):
	packages = []
	package_ids = subprocess.check_output(["pkgutil", "--pkgs"]).decode().split("\n")[:-1]
	for package in package_ids:
		if not include_apple_packages:
			if not package.startswith("com.apple"):
				pkg = Package(**parse_package_info(subprocess.check_output(["pkgutil", "--pkg-info", package]).decode()))
				packages.append(pkg)
		else:
			pkg = Package(**parse_package_info(subprocess.check_output(["pkgutil", "--pkg-info", package]).decode()))
			packages.append(pkg)
	return packages


def parse_package_info(infos):
	result = {}
	for info in infos.split("\n")[:-1]:
		temp = info.split(" ")
		result[temp[0][:-1].replace("-", "_")] = " ".join(temp[1:])
	return result


def get_dead_packages(packages):
	results = []
	for package in packages:
		if package.is_dead:
			results.append(package)
	return results


def forget_package(package):
	subprocess.check_call(["sudo", "pkgutil", "--forget", package.package_id])


def remove_package(package):
	for file in package.files:
		try:
			if os.path.isdir(file):
				shutil.rmtree(file)
			elif os.path.isfile(file):
				os.remove(file)
		except OSError:
			pass
	forget_package(package)
