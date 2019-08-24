Configure interfaces
--------------------

* /etc/network/interfaces

.. code:: shell

 source /etc/network/interfaces.d/*

* /etc/network/interfaces.d/lo

::

 auto lo
 iface lo inet loopback

* /etc/network/interfaces.d/eth0

::

 auto eth0
 iface eth0 inet dhcp
