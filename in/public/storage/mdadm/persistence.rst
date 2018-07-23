Persistence
===========

* reference the device in configuration

.. code:: shell

 mdadm --detail --scan /dev/md0 >> /etc/mdadm/mdadm.conf

* update the initial file system

.. code:: shell

 update-initramfs -u
