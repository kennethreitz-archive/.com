ShowMe v1.0.0 Released
######################

:date: 2010-09-16 05:41
:category: Code


This weekend, I released a new Python module to PyPi: ShowMe
v1.0.0. ShowMe is a simple set of function decorators that give you
easy diagnose common problems in your Python applications. Basic
Usage: ---------- @showme.trace def complex\_function(a, b, c,
\*\*kwargs): ....

::

    >>> complex_function('alpha', 'beta', False, debug=True)
    calling haystack.submodule.complex_function() with
       args: ({'a': 'alpha', 'b': 'beta', 'c': False},)
       kwargs: {'debug': True}

It currently supports: \* Argument call tracing \* Execution Time
(in seconds) \* CPU Execution Time \* Docstrings Roadmap: \* Add
@showme.locals Support \* Add @showme.globals Support Installation
pip install showme
[`Source on GitHub <http://github.com/kennethreitz/showme>`_]
