GistAPI.py v0.1 Released
########################

:date: 2010-05-16 21:41
:category: Code


Today I released GistAPI.py v0.1.2. It features a highly-optimized
Gist object model and API wrapper which allows you to consume Gists
in your next Python application. GitHub just rolled out a miniature
pre-release of the
`Gist API <http://develop.github.com/p/gist.html>`_ last month, so
API functionality is pretty limited at the moment. More features
will be added as soon as the API is updated. ## Usage from gistapi
import \*

::

    gist = Gist('d4507e882a07ac6f9f92')
    
    gist.description          # 'Example Gist for gist.py'
    gist.created_at           # '2010/05/16 10:51:15 -0700'
    gist.public               # False
    gist.filenames            # ['exampleEmptyFile', 'exampleFile']
    gist.files['exampleFile'] # 'Example file content.'

`Source on GitHub <http://github.com/kennethreitz/gistapi.py/>`_
