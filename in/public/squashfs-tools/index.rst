squashfs-tools
==============

Archive
-------

.. code:: shell

 mksquashfs \
 /directory \
 /filesystem.squashfs \
 -b 1m \
 -comp xz

.. todo:: compression options

Unarchive
---------

.. code:: shell

 unsquashfs \
 /filesystem.squashfs

.. todo:: specify output directory's name
