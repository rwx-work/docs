Unprivileged
============

.. warning:: Work In Progress

Mandatory
---------

Configuration
^^^^^^^^^^^^^

* config

::

 lxc.idmap = u 0 100000 65536
 lxc.idmap = g 0 100000 65536

Permissions
^^^^^^^^^^^

.. todo:: shift root's uid for rootfs

Not sure
--------

Packages
^^^^^^^^

::

 uidmap

Configuration
^^^^^^^^^^^^^

* /etc/sysctl.conf

::

 kernel.unprivileged_userns_clone=1

* /etc/subgid
* /etc/subuid

::

 root:100000:65536

* config

::

 lxc.include = /usr/share/lxc/config/userns.conf
 lxc.apparmor.profile = unconfined
