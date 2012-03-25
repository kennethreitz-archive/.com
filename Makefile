
html:
	rm -fr output/*.html output/theme
	./pelican_r -t theme -s settings.py content

ci: init html
	cd output; git add -A; git commit -m 'update'; git push git@heroku.com:kennethreitz.git master

init:
	pip install -r requirements.txt
	mkdir -p output
