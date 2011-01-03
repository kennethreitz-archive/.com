MediaTemple (dv) Backup to S3 Script
####################################

:date: 2009-12-18 14:38
:category: Code


## The Problem `MediaTemple <http://mediatemple.net>`_ servers run
the \*Plesk Control Panel\*, which \*has\* a reputation for having
\*useless backups\*. ## The Solution \* MySQL Dumps of all
Databases and Tables \* All configured vhosts, zipped up \* Pushes
it all to either S3 or FTP Stick it in ``/etc/cron.daily/``, and
you'll be good to go. No more worries. No more headaches. Ever.
\*\*Note:\*\* Standard FTP is also supported. ### The Code:
