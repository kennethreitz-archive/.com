html:
	rm -fr output/*.html
	./pelican_r -t theme -s settings.py content

ci: init html
	cd output; git add -A; git commit -m 'update'; git push git@heroku.com:kennethreitz.git master

init:
	pip install -r reqs.txt
	mkdir -p output
	cd output; git init
	touch output/index.php
	echo 'php_flag engine off' > output/.htaccess