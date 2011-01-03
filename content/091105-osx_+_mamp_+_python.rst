OSX + MAMP + Python + PHP + MySQL 
##################################

:date: 2009-11-05 18:15
:category: Code


If you're a web developer who uses MAMP in conjunction with
anything other than PHP,
I'm sure you've had quite a large bit of frustration involving
multiple MyQL instances.

Not any more! This simple chain of commands will save you days upon
days of troubles:

::

    sudo rm  /tmp/mysql.sock
    sudo ln -s /Applications/MAMP/tmp/mysql/mysql.sock /tmp/mysql.sock

I only wish I had found this sooner. Enjoy.
