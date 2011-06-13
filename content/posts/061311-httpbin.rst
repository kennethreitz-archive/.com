Announcing HttpBin.org
######################

:date: 2011-06-13 01:00
:category: Python
:featured: True
:gh: https://github.com/kennethreitz/httpbin


The development of `Requests <https://python-requests.org>`_, the Python HTTP
Module for Humans, led to some annoying testing practices. Relying on random
websites and services in order to test different capabilities of the HTTP
client became annoying quickly.

`PostBin.org <http://postbin.org>`_ was perfect for testing POST request
behavior, but is usless for other situations. I was hoping to extend its
functionality to other request types, but it turns out that PostBin runs
on the Google App Engine platform. No.

Thus, `httpbin.org <http://httpbin.org>`_ was born.


Example Endpoints
-----------------

To get a feel for what **HttpBin** does, here are a few endpoint examples:

``$ curl http://httpbin.org/ip`` ::

    {"origin": "::ffff:24.127.96.129"}

``$ curl http://httpbin.org/user-agent`` ::

    {"user-agent": "curl/7.19.7 (universal-apple-darwin10.0) libcurl/7.19.7 OpenSSL/0.9.8l zlib/1.2.3"}

``$ curl http://httpbin.org/get`` ::

    {
       "args": {},
       "headers": {
          "Accept": "*/*",
          "Connection": "close",
          "Content-Length": "",
          "Content-Type": "",
          "Host": "httpbin.org",
          "User-Agent": "curl/7.19.7 (universal-apple-darwin10.0) libcurl/7.19.7 OpenSSL/0.9.8l zlib/1.2.3",
          "X-Forwarded-For": "::ffff:24.127.96.129",
          "X-Forwarded-Protocol": ""
       },
       "origin": "::ffff:24.127.96.129",
       "url": "http://httpbin.org/get"
    }

``$ curl -I http://httpbin.org/status/418`` ::

    HTTP/1.1 418 I'M A TEAPOT
    Server: nginx/0.7.67
    Date: Mon, 13 Jun 2011 04:25:38 GMT
    Connection: close
    x-more-info: http://tools.ietf.org/html/rfc2324
    Content-Length: 135


Moving Forward
--------------

**HttpBin** will be packaged and released on PyPi soon, for local development
use and requests-tests runs on `ci.kennethreitz.com <http://ci.kennethreitz.com>`_.
I need to determine a portable pattern for this.

In the coming weeks, I'd like to add a few new new endpoints: ``/deflate``, ``/basic-auth``, *&c*. Contributions are welcome.

I'm considering adding optional request logging / history to the service,
powered by Redis. A new ``/post`` request, for example, would be redirected to
a new URL (e.g. ``/post/c1548ed``) that can be POSTed to repetitively. This
will give **HttpBin** feature parity with postbin.


Source Code
-----------

**HttpBin** is open source (ISC Licensed), and is powered by
`Flask <http://flask.pocoo.org/>`_, `Werkzeug <http://werkzeug.pocoo.org/>`_,
and good intentions.

- `Code on GitHub <https://github.com/kennethreitz/httpbin>`_
- `httpbin.org <http://httpbin.org>`_
