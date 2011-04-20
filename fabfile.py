import os
from fabric.api import *


def build():
	"""Builds website."""
	local('pelican -t theme -s settings.py content')
	# mv index archive.html
	# take out all but 8 latest articles
	os.chdir('html')
	os.system('rm -fr feeds category pages tag theme')
	os.system('mv ../output/* .')
	os.system('git add -A')
	os.system('git commit -m \'content update\'')
	os.system('git push origin gh-pages')

# def docs():
# 	"""Build docs."""
# 	os.system('make html')
# 	os.chdir('_build/html')
# 	os.system('sphinxtogithub .')
# 	os.system('git add -A')
# 	os.system('git commit -m \'documentation update\'')
# 	os.system('git push origin gh-pages')
