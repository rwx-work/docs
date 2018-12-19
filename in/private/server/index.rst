Server
======

Hardware
--------

Partition
---------

.. code:: shell

 parted

 select /dev/sda
 mktable gpt
 mkpart raid 1 2000364
 mkpart boot 2000364 2000399
 toggle 2 boot

 select /dev/sdb
 mktable gpt
 mkpart raid 1 2000364
 mkpart boot 2000364 2000399
 toggle 2 boot

 q

.. code:: shell

 mdadm --create /dev/md0 \
 --level 0 --raid-devices 2 /dev/sd[ab]1

.. code:: shell

 parted /dev/md0

 mktable gpt
 mkpart data 1 3966099
 mkpart swap 3966099 4000458

 q

.. code:: shell

 mkfs.ext4 -L data /dev/md0p1
 mkswap --label swap /dev/md0p2
