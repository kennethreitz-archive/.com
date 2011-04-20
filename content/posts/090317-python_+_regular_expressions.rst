Python + Regular Expressions
############################

:date: 2009-03-17 05:30
:category: Code


Have you ever needed to parse through large amounts of text looking
for a specific pattern? Patterns like “one capital letter followed
by three numbers” or “dd/mm/yyyy”? This is known as Pattern
Matching. Regular Expressions allow easy syntax for pattern
matching, and is an invaluable skill to add to one’s toolkit, no
matter what your area of expertise/practice is. Whether you’re
writing a Compiler, Form Validator, Text Editor, Django Project, or
Language Translator, Regular Expressions will always prove to be
invaluable. Here is a very basic overview of some syntax: ‘\\d’
represents a digit. ‘\\s’ represents whitespace. ‘.’ represents any
character. If you have worked with Python for very long, you are
probably already familiar with the concept. Take a look at the
following code::

    print("Rounded = %05d" % (42))

This makes sure that the digit printed has 5 digits, and will
automatically add 0’s to compensate. If you understand this
concept, then you shouldn’t have a problem. Perl-style Regular
Expressions are a very widely-accepted implementation, and Python
has built in support for this mini-language! It’s easily
accessible, so let’s get started. The included ‘re’ module will
give us everything we need to get started: import re

Lets give our new module a try! It will enable you to do anything
you could ever want with regular expressions. Here’s a quick
example of some basic use::

    import re

    string0 = 'Kenneth Reitz is a cool guy!'
    regExp = r’kenneth[- ]?reitz’

    if re.match(regExp, string0, re.IGNORECASE):
       print “True”
    else:
       print “False”


This script takes the string ``'Kenneth Reitz is a cool guy'``, and
searches for ``'kenneth reitz'`` inside of it. If ‘kenneth reitz’ is
found within string0 (re.match compares the expression with the
string), the script will print ``True``, if not, it will print
``False``. Additional parameters can be passed to the re.match
function when needed. Note the ``re.IGNORECASE`` flag used here –-
This tells the function be case-insensitive. Once you master the
regular expression syntax, you’ll realize how truly powerful they
can be. The options become limitless and the usefulness becomes
undeniable. Here’s another example::

    import re

    string0 = '10.03.1988'
    regExp = r'^\d\d[./]\d\d[./]\d\d\d\d?$'

    if re.match(regExp, string0):
       print 'True'
    else:
       print 'False/


When run, this script prints out ``True``. If we were to change
string0 to ``‘10.03.88’``, it would print ``False``. Simple, isn’t it?
Now, while a True/False return could be useful in certain
applications (i.e. form validation), most of the time, we’re going
to want to have a bit more information in order for our checks to
be useful. We can tell Python to show us the data that matches our
query. To do this, we’re going to have to break our expression up
into different groups. In the date we have defined, there are three
obvious groups we could separate this into: the day, month, and
year. While defining a Regular Expression, you can use parentheses
to define groups: ``regExp = r’^()././$’``

This separates our expression into 3 separate groups. Python also
supports turning a Regular Expression string into an
heavily-supported object with the re.compile() function. Once you
define a string as a Regular Expression object, you can use the
built in methods to preform powerful parsing. Now we can ask python
what is in those groups::

    import re

    string0 = ‘10.03.1988’

    regExp = re.compile(‘^()././$’)
    regExpMatches = regExp.match(string0)

    if re.match(regExp, string0):
       print(“Day: %s\nMonth: %s\nYear: %s” % (regExpMatches.group(1), \
         regExpMatches.group(2), regExpMatches.group(3)))
    else:
       print(“Invalid Date.”)


When executed, this script parses through our validated date,
breaks it down into groups, and prints the following::

    Day: 10
    Month: 03
    Year: 1988


The possibilities are limitless! Here’s a quick run-down of the re
module’s functions, strait from the Python documentation for
reference: match: Match a regular expression pattern to the
beginning of a string. search: Search a string for the presence of
a pattern. sub: Substitute occurrences of a pattern found in a
string subn: Same as sub, but also return the number of
substitutions made. split: Split a string by the occurrences of a
pattern. findall: Find all occurrences of a pattern in a string.
compile: Compile a pattern into a RegexObject. purge: Clear the
regular expression cache. escape: Backslash all non-alphanumerics
in a string.

Remember, you can always type help(re) (after importing the re
module) into the Python interpret to take a quick look at the
module’s built-in documentation. Good luck and happy coding!
