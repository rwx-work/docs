****
Host
****

Check
=====

.. code:: shell

  lxc-checkconfig

List
====

.. code:: shell

  lxc-ls -f

.. code:: shell

  lxc-ls --fancy

Network bridge
==============

Create bridge br0 onto host's network interface eth0:

* /etc/network/interfaces.d/eth0

::

  auto br0
  iface br0 inet static
      address host_ip/network_mask_bits
      gateway gateway_ip
      bridge_fd 0
      bridge_maxwait 0
      bridge_ports eth0
      bridge_stp on

Service
=======

Default configuration for new containers:

* /etc/lxc/default.conf

.. code:: ini

  lxc.include = /usr/share/lxc/config/debian.common.conf

  lxc.arch = amd64
  lxc.autodev = 1
  lxc.kmsg = 0
  lxc.rootfs.backend = dir
  lxc.start.auto = 1

  lxc.network.type = veth

  lxc.network.flags = up
  lxc.network.link = br0
  lxc.network.name = eth0

Directories
===========

* 1 for the containers
* 1 for their data

.. code:: shell

  mkdir --parents "containers/directory"
  rmdir "/var/lib/lxc"
  ln --symbolic "containers/directory" "/var/lib/lxc"

.. code:: shell

  mkdir --parents "data/directory"
