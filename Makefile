html:
	rm -fr output/*
	./pelican_r -t theme -s settings.py content

init:
	pip install -r reqs.txt