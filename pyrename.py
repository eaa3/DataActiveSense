# !/usr/bin/python

import os, sys

# listing directories
files = os.listdir(os.getcwd())
print "The dir is: %s"%files

# renaming directory ''tutorialsdir"
for f in files:
	idx=f.find("-")

	if idx > 0:
		modified = f.replace(f[0:idx],"all_data")
		print modified
		os.rename(f,modified)

print "Successfully renamed."

# listing directories after renaming "tutorialsdir"
print "the dir is: %s" %os.listdir(os.getcwd())\