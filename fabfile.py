import os
from fabric.api import *


def build():
	""" Death to the bytecode! """
	local('rm -fr output')
	local('pelican -t theme -s settings.py content')
	# mv index archive.html
	# take out all but 8 latest articles
	local('open output/index.html')

# def docs():
# 	"""Build docs."""
# 	os.system('make html')
# 	os.chdir('_build/html')
# 	os.system('sphinxtogithub .')
# 	os.system('git add -A')
# 	os.system('git commit -m \'documentation update\'')
# 	os.system('git push origin gh-pages')
