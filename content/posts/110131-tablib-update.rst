Tablib Community Update
#######################

:date: 2011-01-31 01:22
:category: code, python
:featured: True


Just wanted to give everyone a quick update on the status of Tablib and its future. Updates will be more regular in the future.

For those unfamiliar with Tablib, it’s my format-agnostic tabular data library. To learn more, see `Tablib.org <http://tablib.org>`_.


Since its release, Tablib has been installed over 2,500 times (from PyPi alone), has 124 watchers on GitHub, and multiple contributors. It is now being used in production at major corporations and development shops throughout the world, including: The Library of Congress, National Geographic, and Discovery Channel.. If your company is using Tablib, feel free to let me know!

Typical case reports include: presenting customer data, statistical data export/manipulation, sampling systems, personal finance management/calculation, and much more.

The community reaction to the initial release was more than I had hoped for. My Changelog article was trending for days on HackerNews, Reddit, and GitHub. This brought quite a few emails, bug reports, and contributions. I was quite surprised, considering documentation hadn’t even been written yet!

Needless to say, the project has significantly matured since. New features and infrastructure include:


    - Extensive documentation (http://tablib.org)
    - Extensive Unittesting + Continuous Integration System
    - Transposition
    - Databook support (e.g. Excel workbooks w/ multiple sheets)
    - Row & Column appends
    - Validation hooks
    - Advanced unicode (Python 2.x)
    - Row objects w/ tags
    - Section separators
    - Dataset sorting and filtering
    - Pickling Support
    - Improved XLS formatting w/ header frames and newline handling
    - No dependencies, all modules needed are vendorized
    - Advanced format support framework

A handful of these features have been provided by the work of a few generous contributors.

    - Luke Lee
    - Luca Beltrame
    - Josh Ourisman


Also worth mentioning is the excellent `django-tablib <https://github.com/joshourisman/django-tablib>`_ extension by Joshua Ourisman. It allows you to seamlessly generate Tablib Datasets from Django QuerySets.


The Future of Tablib
~~~~~~~~~~~~~~~~~~~~

Right now, Tablib’s biggest weakness, ironically, is tabular data’s biggest strength: big data. If you have experience dealing with big data in Python (e.g. 8GiB+ CSV files), I’d love to get your insight on how to proceed.

I will doing a lighting presentation on Tablib at PyCon 2011 in Atlanta, GA this March. I hope to increase awareness, gather feedback/suggestions, and recruit big data developers to assist.

Also planned is the tablib-extras project. The plan is to support various backends, like Google Fusion Tables, and a SQLAlchemy Mapper.

[`Tablib.org <http://tablib.org>`_]
[`Source on GitHub <https://github.com/kenethreitz/tablib>`_]
[`PyPi <http://pypi.python.org/pypi/tablib>`_]