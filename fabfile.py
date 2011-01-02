import os
from fabric.api import *

os.f
def build():
	""" Death to the bytecode! """
	local('pelican -t krtheme -s settings.py .')

# def docs():
# 	"""Build docs."""
# 	os.system('make html')
# 	os.chdir('_build/html')
# 	os.system('sphinxtogithub .')
# 	os.system('git add -A')
# 	os.system('git commit -m \'documentation update\'')
# 	os.system('git push origin gh-pages')