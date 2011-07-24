Requests v0.5.1 Released
########################

:date: 2011-07-24 02:00
:category: python
:featured: True
:gh: https://github.com/kennethreitz/requests


Requests v0.5.1 was just released.

If you're unfamiliar with **Requests**, it is the HTTP Module for Humans. It
strives to keep things as simple as possible. `Learn more <http://python-requests.org>`_.


Community Update
----------------

I'm really happy with the direction that Requests is going. The repo is
approaching `400 watchers on GitHub`_ (trailing just behind the Pyramid
framework), and has been downloaded over 1100 times from PyPi in the last
month alone.

If you head over to `python-requests.org <http://python-requests.org>`_,
you'll be greeted by the new Requests mascot, Rez the sea turtle.

This October, I'll presenting at `PyCodeConf <http://py.codeconf.com/>`_
in Miami, FL. Topics will include Requests' API design and how libraries
like it help to make Python more accessible.

**API Design and Pragmatic Python**

    Unfortunately, solving simple problems with Python isn't always
    ``import antigravity``. This talk will analyze the high barriers of
    entry that clutter the Python landscape. We'll discuss ways to make
    Python more accessible for newcomers and less of a headache for
    seasoned veterans.


If you are using Requests in a project, `let me know <mailto:me@kennethreitz.com>`_

New Features
------------

The v0.5.x series has brought along some awesome features so far:

- ``PATCH`` Support!
- International Domain Name Support!
- Forced Basic Authentication (for 404'd responses; default)
- Querystrings available for all methods
- ``python-requests.org`` default User-Agent header
- Sexy HTTPBin Test Suite
- ``settings.verbose`` configurable stream for debugging and logging.
- Access response headers without fetching entire body (``read()``)
- Use lists as dicts for parameters w/ multiple values
- Dict-configurable Proxies
- ``Accept-Encoding: gzip`` default on.


Moving Forward
--------------

In the short-term, I plan to remove Request's dependency on Poster, and
replace the multipart file upload functionality with internal code.

Once Poster is removed, Python3.1+ support will be added.

Once the port to Python3 is complete, elegant HTTPS certificate checking will

While those development tasks are being carried out, I'm planning on adding
some more exhaustive documentation to the website: tutorials, FAQ, use
cases recipes, scenarios, &c.


Source Code
-----------

**Requests** is open source (ISC Licensed), and will make you life awesome.

- `Code on GitHub <https://github.com/kennethreitz/legit>`_
- ``_