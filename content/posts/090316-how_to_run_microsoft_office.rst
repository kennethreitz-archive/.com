How to Run Microsoft Office 2007 in Ubuntu Linux 8.10
#####################################################

:date: 2009-03-16 19:12
:category: Code


|ms-office-2007| Wouldn't it be lovely to have a nice, clean
installation of Microsoft's Office 2007 Suite to run on your Ubuntu
Linux Distribution? For some people, this is the only thing that
truly holds them back from an all-Linux environment... But not
anymore! We have compiled a nice, concise set of instructions to
help guide you along. ### Install Wine:

WINE (**W**ine **I**s **N**ot an **E**mulator) is an application
layer for Linux that interprets the Windows API and DLLs into
native Linux commands. This allows for programs made for Windows to
be run in Linux! In order to run Office 2007, Wine 1.1.9 (or newer)
is **required.** It is currently in a development release. If you
don’t have it installed already (this is very likely), go ahead and
type the following commands, which will set it up for you: wget -q
http://wine.budgetdedicated.com/apt/387EE263.gpg -O- \| sudo
apt-key add -

::

    sudo wget http://wine.budgetdedicated.com/apt/sources.list.d/intrepid.list -O /etc/apt/sources.list.d/winehq.list
    
    sudo apt-get update
    
    sudo apt-get install wine cabextract

**NOTE**:
*On non-Debian based systems, this will not work. Please refer to*
`*this site* <http://www.winehq.org/site/download-deb>`_
*for installation instructions.* You should now have an
installation of Wine 1.1.9 installed on your system. To confirm the
version of Wine installed, type the following: wine --version

Install winetricks:
~~~~~~~~~~~~~~~~~~~

`Winetricks <http://www.kegel.com/wine/winetricks>`_ is a small SH
script which will go on the internet and automatically fetch and
install Microsoft DLLs and Libraries into Wine with almost no
hassle at all! To download it directly, type the following
commands: wget http://www.kegel.com/wine/winetricks

::

    chmod +x ./winetricks

Utilize winetricks:
~~~~~~~~~~~~~~~~~~~

This will setup all necessary libraries and DLLs that Office 2007
will need to run properly: ./winetricks gdiplus riched20 riched30
msxml3 msxml4 msxml6 corefonts tahoma vb6run vcrun6 msi2

Please be patient while the downloads complete. This script is
working hard and is saving hours of your time. ### Insert Office
2007 Disk and Run Setup!

Now that we have all of the DLLs necessary to run the Installer,
let us do so! wine pathToCD/setup.exe

From here on out, you should be good to go! The installer should
run and install everything just as if it was a Windows system! If
you have any problems, ask, and we'll try to help you out as much
as possible! UPDATE: Lost your CD?
`Download the installer <http://www.programmerfish.com/free-direct-download-microsoft-office-2007>`_
for free!

.. |ms-office-2007| image:: http://www.programmerfish.com/wp-content/uploads/2009/03/msoffice2007.gif