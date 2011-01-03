Django Remote Development Server
################################

:date: 2009-05-08 04:03
:category: Code


|image| If you've worked with Django much at all, I'm sure you've
had this problem: wanting to access the built-in development
webserver remotely. Typically, this integrated mini-server ignores
all requests from any IP Address other than 127.0.0.1 . If you run
the following command, however, it will be accessible remotely.
VERY useful for remote dev work.

::

    ./manage.py runserver 0.0.0.0:8000

Enjoy!

`Development <http://technorati.com/tag/Development>`_,
`Django <http://technorati.com/tag/Django>`_,
`Python <http://technorati.com/tag/Python>`_

.. |image| image:: http://media.kennethreitz.com/images/django-logo.png