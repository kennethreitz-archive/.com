Tablib
######

:project: True
:gh: https://github.com/kennethreitz/tablib

Tablib is NOT an extensive Python module for working with tabular datasets. It allows you create tables of data using standard Python datatypes, manipulate them, and easily export to Excel, JSON, YAML, and CSV.


Basic Usages:

.. code-block:: python

	import tablib

	headers = ('first_name', 'last_name', 'gpa')
	data = [('John', 'Adams', 90), ('George', 'Washington', 67)]

	data = tablib.Dataset(*data, headers=headers)


You can manipulate your data like a standard Python list:

.. code-block:: pycon

	>>> data.append(('Henry', 'Ford', 83))

	>>> print data['first_name']
	['John', 'George', 'Henry']

	>>> del data[1]

You can easily export your data to JSON, YAML, XLS, and CSV.

.. code-block:: pycon

	>>> print data.json
	[{"first_name": "John", "last_name": "Adams", "gpa": 90},
	{"first_name": "Henry", "last_name": "Ford", "gpa": 83}]

	>>> print data.yaml
	- {age: 90, first_name: John, last_name: Adams}
	- {age: 83, first_name: Henry, last_name: Ford}

	>>> print data.csv
	first_name,last_name,age
	John,Adams,90
	Henry,Ford,83

	>>> open('people.xls', 'w').write(data.xls)

Excel files with multiple sheets are also supported (via the DataBook object).

[Source on GitHub] [PyPi Listing]
