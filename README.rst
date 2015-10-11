PackageUtil
===========

PackageUtil is a simple command line tool for OS X that rids you of the pain that is pkgutil.
It can:

- Deletes packages and their associated files
- Detect and delete dead packages
- Lists packages
- Lists dead packages

Usage
-----
.. code:: bash
	
	$ packageutil

+-------------------------------+---------------------------------------+
| -pkgs				| Lists all packages.			|
+-------------------------------+---------------------------------------+ 
| -dead-pkgs			| Lists all dead packages.		|
+-------------------------------+---------------------------------------+ 
| -rm				| Remove package by name.		|
+-------------------------------+---------------------------------------+ 
| -ls				| List files of package.		|
+-------------------------------+---------------------------------------+
| --forget-dead-pkgs		| Forgets all dead packages.		|
+-------------------------------+---------------------------------------+
| --include-apple-pkgs		| Should Apple packages be included?	|
+-------------------------------+---------------------------------------+ 

Installation
------------
- pip
	.. code:: bash
		
		pip install packageutil

- Manual
	.. code:: bash
		
		git clone https://github.com/PhilipTrauner/PackageUtil
		cd PackageUtil
		python setup.py install
