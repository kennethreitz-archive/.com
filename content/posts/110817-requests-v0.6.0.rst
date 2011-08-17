Requests v0.6.0 Released!
#########################

:date: 2011-08-17 05:20
:category: python
:featured: True
:gh: https://github.com/kennethreitz/requests


Requests v0.6.0 was just released! This is big.

If you're unfamiliar with **Requests**, the Python HTTP Module for
Humans, it strives to keep things as simple and elegant as possible.
`Learn more <http://python-requests.org>`_.

The Highlights
--------------

Sessions
~~~~~~~~

I'm extremely happy to announce that Requests now has support for sessions!

A session is created with a simple context manager. The resulting object
has a method for each type of request, just like Requests itself.

Any optional parameters can be passed to ``requests.session``, and will
be included in each Request method call. Cookies are also persisted
throughout all requests within a session.

::

    with requests.session(auth=('username', 'password')) as s:

        r = s.get('https://api.github.com')

        r.status_code
        # 200


`Learn more about sessions
<http://docs.python-requests.org/en/latest/user/advanced/#session-objects>`_.


Status Code Reference
~~~~~~~~~~~~~~~~~~~~~

When reading HTTP code, remembering the exact meaning for every
status_code can be difficult. Especially if you're working with a robust
API. So, I've included a flexible lookup object to reference a status_code
within your code.

::

    >>> requests.codes.ok
    200

    >>> requests.codes.IM_A_TEAPOT
    418

    >>> requests.codes['precondition_failed']
    412


Dict Cookies
~~~~~~~~~~~~

Requests has had CookieJar support for a while, but that's far from ideal.
CookieJars require an enormous amount of manual code. So, now you can give
Requests a simple dictionary wherever it expects a CookieJar, and it'll
automatically generate a CookieJar for you!

Best yet, if a server responds with Cookies in any request, you'll have
a simple dictionary waiting for you in ``Response.cookies``. If you
want the full CookieJar, you can access it at ``Response.request.cookiejar``.


Hook System
~~~~~~~~~~~

I've added a new hooks system for both signaling and modifying the
method arguments, requests, and responses during the request lifecycle.

This will be extremely useful for using Requests to wrap web service APIs.
Adding custom authentication mechanisms (OAuth anyone?) should be as simple
as a few callbacks within a session.

`Learn more about Hooks
<http://docs.python-requests.org/en/latest/user/advanced/#event-hooks>`_.


*&c*
~~~~

I saw a large number of users relying on the order of the request
function parmaters, instead of naming the arguments explicitly.
So, now everything but ``url`` (and sometimes ``data``) is passed
via ``**kwargs``, so you have to do things properly. This also gives me
some flexiblity in making API decisions in the future.



Community Update
----------------

This weekend, Requests had its biggest explosion ever. The documentation has
been accessed 43,000+ times by 25,000+ unique visitors in the past 30 days.
The repo is approaching `700 watchers on GitHub
<https://github.com/kennethreitz/requests>`_ (trailing just behind Celery),
and the latest release has been downloaded over 2000 times from PyPi in
the last month alone.

Another big milestone: we now have 25 contributors! Many thanks to everyone
involved :)


Changelog
---------

Here's a full list of what's new on v0.6.0:

- New callback hook system
- New persistent sessions object and context manager
- Transparent Dict-cookie handling
- Status code reference object
- Removed Response.cached
- Added Response.request
- All args are kwargs
- Relative redirect support
- HTTPError handling improvements
- Improved https testing
- Bugfixes


Source Code
-----------

**Requests** is open source (ISC Licensed), and will make your world a
better place. I promise :)

- `Code on GitHub <https://github.com/kennethreitz/requests>`_
- `python-requests.org <http://python-requests.org>`_