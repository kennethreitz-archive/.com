#!/usr/bin/env python
# -*- coding: utf-8 -*-


""" KennethReitz.com Importer
    Generates ReST files from a WXR file.
"""

import io
import os
import sys

import lxml
import pandoc
from django.utils.encoding import smart_str, smart_unicode
from lxml import etree


# python-dateutil
from dateutil.parser import parse as dtime 



class Post(object):
	"""A blog post"""

	def __init__(self):
		self.title = None
		self.published = None
		self.content = None
		self.id = None



posts = []

try:
	in_file = sys.argv[1]
except IndexError:
	print 'Specify a file.'


parser = lxml.etree.XMLParser(recover=True) #recovers from bad characters.
tree = lxml.etree.parse(in_file, parser)

for post in tree.iterfind('//item'):
	p = Post()
	p.title = post.find('title').text
	p.published = dtime(post.find('pubDate').text)
	p.content = post.find('{http://purl.org/rss/1.0/modules/content/}encoded').text

	posts.append(p)


os.system('mkdir -p content')
os.chdir('content')



for post in posts:
	#print '- %s' % post.title
	#print post.__dict__
	filename = post.published.strftime('%y%m%d-')
	filename = filename + '_'.join(post.title.split()[:5]).lower()
	for char in ('?', '\'', ':', '.', ''):
		filename = filename.replace(char, '')
	filename += ('.rst')


	content = pandoc.Document()
	content.html = smart_str(post.content)

	_buffer= str(content.markdown)

	content.markdown = _buffer

	article = post.title + '\n'
	article += '#' * len(post.title) + '\n\n'
	article += ':date: %s\n' % post.published.strftime('%Y-%m-%d %H:%M')
	article += ':category: Code\n\n\n'

	article += content.rst
	

	with open(filename, 'w') as f:
		f.write(article)



