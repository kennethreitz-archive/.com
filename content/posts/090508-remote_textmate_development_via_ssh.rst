Remote TextMate Development via SSH and Rsync
#############################################

:date: 2009-05-08 00:39
:category: Code


I am a huge fan of
`TextMate <http://kennethreitz.com/blog/if-textmate-42/>`_. In my
opinion, it is by far the greatest text editor ever conceived by
mankind. It has a couple of shortcomings, however. One of which is
that it has no built-in FTP or SFTP support. Remote file editing is
a bit of a bear here if you like to view folders in the project
drawer on the side. |image|
**Options for remote editing with TextMate:** - Cyberduck FTP
client - MacFUSE + SSHFS - Rsync + SSH

Cyberduck
---------

**The `Cyberduck <http://david.olrik.dk/files/Synchronize_remote_directory_rsync_ssh.zip>`_ option is very very useful. While in the FTP client, you simply click "Edit in TextMate" and the client will download the file for you, open it in your editor, and – here's the awesome part – it automatically uploads the file every time you save it. This works great when working with one file at a time. The drawback, however, is when working with large projects. Toggling between many files can be an albatross without the project drawer (cyberduck understandably doesn't allow you to edit an entier folder), so MacFUSE is the next logical choice.**
## MacFUSE + SSHFS

`MacFUSE <http://www.pqrs.org/tekezo/macosx/sshfs/>`_ + SSHFS works
great, and allows you to mount an SSH folder as a mountpoint on
your local system. VERY USEFUL. You can open this folder with
TextMate. This is perfect for smaller projects. However, with
larger projects, this makes opening the folder in TextMate almost
unbearable as it checks the status of every single file. Too slow
:P ## Rsync + SSH

**So here's the final solution: Rsync + SSH. This allows me to automatically sync my working copy with my server and allow for snappy file interactions without having insane latencies for starting up and bandwidth hogging!**
To remotely sync over SSH, run the following code: rsync -avz -e
ssh remoteuser@remotehost:/remote/dir /target/dir/

**Hint**: If your remote working copy is a subverson checkout, you
can add --cvs-exclude

into the rsync parameters, and it will exclude the ".svn" folders!
You can then open this directory in TextMate and make all the
changes you want, and then sync after ! There is also a wonderful
TextMate Bundle for
`Remote Rsync + SSH within TextMate <http://david.olrik.dk/files/Synchronize_remote_directory_rsync_ssh.zip>`_.
`Development <http://technorati.com/tag/Development>`_,
`OSX <http://technorati.com/tag/OSX>`_,
`rsync <http://technorati.com/tag/rsync>`_,
`TextMate <http://technorati.com/tag/TextMate>`_

.. |image| image:: http://media.kennethreitz.com/images/textmate-logo.png