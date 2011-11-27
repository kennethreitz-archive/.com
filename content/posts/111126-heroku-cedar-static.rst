Static Sites on Heroku Cedar
############################

:date: 2011-11-26 05:20
:category: python
:featured: True

Heroku's excellent `Cedar Stack <http://devcenter.heroku.com/articles/cedar>`_
has first-class support for Python, Ruby, Node.js, Java, Clojure, and Scala applications.
Unfortunately, there's no obvious way to serve static sites without first
fronting them with a Rack or WSGI application.

The Cedar stack has unofficial support for
`Custom Build Packs <https://github.com/heroku/heroku-buildpack-python>`_,
which allow you to compile your own language runtime on top of Cedar.
My plan was to build an custom nginx build pack for Cedar, but that turned out
to be completely unnecessary.

Did you you know that Cedar has full (unofficial)
support for PHP applications, fronted with Apache? When you push up a repository
with an ``index.php`` file at the root, Apache and PHP are bundled into
your application at runtime.

Elegant Static Sites on Cedar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First, lets turn your site into a PHP "application"::

    $ touch index.php

Next, we can fully disable Apache's PHP engine::

    $ echo 'php_flag engine off' > .htaccess

When you push this up, you'll have a bare Apache instance serving up the
contents of your site to the world. Best yet, you can do all of the
`stupid .htaccess tricks <http://perishablepress.com/press/2006/01/10/stupid-htaccess-tricks/>`_
that you could on on any traditional shared hosting platform.

It works great! This very website is served this way.