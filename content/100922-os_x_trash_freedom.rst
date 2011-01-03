OS X Trash Freedom
##################

:date: 2010-09-22 19:46
:category: Code


I noticed today that i had 120GiB of data in my Mac's Trashcan. I
had enough. so I tried to kill it, and discovered a nice hidden
feature. rm -fr ~/.Trash ln -s /dev/null ~/.Trash

Now, when you delete a file in Finder, you get a nice pop-up
warning that the file will be permanently deleted.
`|image| <http://media.kennethreitz.com/blog/wp-content/uploads/Screen-shot-2010-09-22-at-3.44.33-PM.png>`_
Bliss. ### Update (Setember 25th, 2010): As it turns out, OS X
defaults to this behavior whenever ~/.Trash is unwritable as a
folder. If you were to place any file in ~/.Trash, you would see
the same behaviour. Oh well, it's still rather useful in function.

.. |image| image:: http://media.kennethreitz.com/blog/wp-content/uploads/Screen-shot-2010-09-22-at-3.44.33-PM.png