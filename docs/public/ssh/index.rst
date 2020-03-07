ssh
===

====== ==============
debian openssh-client
====== ==============

Configure
---------

* /etc/ssh/ssh_config

.. todo:: lines

Create key
----------

* ~/.ssh/id_rsa*

.. code:: shell

  ssh-keygen -b 4096

.. todo:: other arguments

Tunnel
------

.. code:: shell

 ssh -N -D local_port domain.tld
