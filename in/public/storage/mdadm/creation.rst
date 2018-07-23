Creation
========

.. warning::

 Only use partitions, never whole devices,
 otherwise assembly will fail after reboot!

RAID 0
------

.. code:: shell

 mdadm --create /dev/md0 --level=0 \
 --raid-devices=2 /dev/sd[bc]1

RAID 1
------

.. code:: shell

 mdadm --create /dev/md0 --level=1 \
 --raid-devices=2 /dev/sd[bc]1

RAID 5
------

.. code:: shell

 mdadm --create /dev/md0 --level=5 \
 --raid-devices=3 /dev/sd[b-d]1
