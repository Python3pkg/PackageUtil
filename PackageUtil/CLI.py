import argparse
from . import PackageUtil
from . import Logging
import os

def main():
	parser = argparse.ArgumentParser(description="Clean up and uninstall OS X packages with ease.")
	parser.add_argument("-pkgs", action="store_true", help="Lists all packages.")
	parser.add_argument("-dead-pkgs", action="store_true", help="Lists all dead packages.")
	parser.add_argument("-rm", nargs='*', help="Remove package by name.")
	parser.add_argument("-ls", nargs='*', help="List files of package.")
	parser.add_argument("--forget-dead-pkgs", action="store_true", help="Forgets all dead packages.")
	parser.add_argument("--include-apple-pkgs", action="store_true", help="Should Apple packages be included?")
	args = parser.parse_args()
	help_required = True
	if args.rm:
		if os.geteuid() != 0:
			Logging.error("Please run as root.")
			exit(1)
		packages = PackageUtil.get_installed_packages(include_apple_packages=args.include_apple_pkgs)
		for package_name in args.rm:
			for package in packages:
				if package.package_id == package_name:
					PackageUtil.remove_package(package)
		help_required = False
	if args.forget_dead_pkgs:
		if os.geteuid() != 0:
			Logging.error("Please run as root.")
			exit(1)
		for package in PackageUtil.get_dead_packages(PackageUtil.get_installed_packages(include_apple_packages=args.include_apple_pkgs)):
			PackageUtil.forget_package(package)
		help_required = False
	if args.ls:
		packages = PackageUtil.get_installed_packages(include_apple_packages=args.include_apple_pkgs)
		for package_name in args.ls:
			for package in packages:
				if package.package_id == package_name:
					for file in package.files:
						print(file)
					print(("Summary: %s" % package.common_prefix))
		help_required = False
	if args.pkgs:
		for package in PackageUtil.get_installed_packages(include_apple_packages=args.include_apple_pkgs):
			print(package)
		help_required = False
	if args.dead_pkgs:
		if os.geteuid() != 0:
			Logging.error("Please run as root.")
			exit(1)
		for package in PackageUtil.get_dead_packages(PackageUtil.get_installed_packages(include_apple_packages=args.include_apple_pkgs)):
			print(package)
		help_required = False
	if help_required:
		parser.print_help()


if __name__ == "__main__":
	main()
