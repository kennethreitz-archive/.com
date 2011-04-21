Requests: Python HTTP Module
############################

:date: 2011-02-19 01:22
:category: python
:featured: True

I’m happy to announce the release of my latest Python module: **Requests**.

One of the most frustrating experiences I have to face, as a Python developer, is the pain of making HTTP requests. The available APIs are insane. I have to look up everything that I want to do and constantly refer to the documentation. I skip writing fun tools from time to time, simply because I don’t want to go through the pain of making a simple PUT request with Basic Authentication.

Things shouldn’t be this way. Not in Python.


Enter Requests
~~~~~~~~~~~~~~

::

    import requests

Let’s check out the awesome new Convore API. ::

    >>> r = requests.get('https://convore.com/api/account/verify.json')
    >>> r.status_code
    401

Oops, we need to be authenticated. Let’s add our credentials and try again. ::

    >>> conv_auth = requests.AuthObject('requesttest', 'requesttest')
    >>> r = requests.get('https://convore.com/api/account/verify.json', auth=conv_auth)
    >>> r.status_code
    200

It worked! Let’s poke around. ::

    >>> r.headers['content-type']
    'application/json'

    >>> r.content
    '{"username": "requeststest", "url": "/users/requeststest/", "id": "9408", "img": "censored-long-url"}'

Requests is capable of much more than this, but the API stays this simple throughout.


Features
~~~~~~~~

Requests strives to be as simple yet powerful as possible. It’s designed to fit the 90% use case. You might not be able to add proxies, client caching, and raw socket access, but you will have everything you need most of the time:

- Extremely simple GET, HEAD, POST, PUT, DELETE requests
- Receive simple response header dictionary, content, and status code
- Module-level HTTP Auth registry
- Eventlet/Greenlet support

The API is quite simple:

- 5 main functions: get(), head(), post(), put(), and delete()
- Attach params/data
- Add HTTP Basic Authentication with a parameter
- Add a dictionary of HTTP headers with a parameter
- Add a CookieJar with a parameter
- Attach File uploads with a parameter


Installation
~~~~~~~~~~~~

To install Requests, simply::

    $ pip install requests

Or, if you must::

    $ easy_install requests

But, you really shouldn’t do that.


Roadmap
~~~~~~~

Requests currently supports CPython 2.5, 2.6, 2.7, and PyPy-c v1.4.

In the future, Python 3.x will be supported. There are no intentions to support Python 2.4 and older.

If you’d like to help or have a feature suggestion, fork me!


[`Source on GitHub <http://github.com/kennethreitz/requests>`_]
[`PyPi Listing <http://pypi.python.org/pypi/requests>`_]
