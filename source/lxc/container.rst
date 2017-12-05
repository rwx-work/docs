*********
Container
*********

TODO
====

* look for creation through debootstrap

Create
======

.. code:: shell

  lxc-create \
  --name="container_name" \
  --template="debian" \
  -- \
  --release="stretch" \
  --mirror="file:/mirrors/debian/debian-stretch" \
  --security-mirror="file:/mirrors/debian/debian-stretch-security" \

Configure
=========

In containers/directory/container_name :

* config

.. code:: ini

  lxc.include = /usr/share/lxc/config/debian.common.conf

  lxc.arch = amd64
  lxc.autodev = 1
  lxc.kmsg = 0
  lxc.mount = /var/lib/lxc/container_name/fstab
  lxc.rootfs = /var/lib/lxc/container_name/rootfs
  lxc.rootfs.backend = dir
  lxc.start.auto = 1
  lxc.utsname = hostname

  lxc.network.type = veth

  lxc.network.flags = up
  lxc.network.link = br0
  lxc.network.name = eth0
  lxc.network.veth.pair = container_name
  lxc.network.hwaddr = virtual_mac_address

Static addresses variant:

.. code:: ini

  lxc.network.ipv4 = container_ip4/network_mask_bits
  lxc.network.ipv6 = container_ip6

* fstab

.. warning::

  | Do not forget to create the data directories
  | otherwise the container start process will fail!

::

  data/directory/container_name data none bind,create=dir
  /mirrors mirrors none bind,create=dir

* rootfs/

    * TODO Debian configuration

* rootfs/etc/network/interfaces.d/eth0

    if the container uses DHCP:

::

  auto eth0
  iface eth0 inet dhcp

Start
=====

.. warning::

  | Be patient, for it can take a container
  | up to 1 minute to get its network stack up!

.. code:: shell

  lxc-start -n "container_name"

.. code:: shell

  lxc-start --name="container_name"

Run command
===========

.. code:: shell

  lxc-attach -n "container_name" -- command

.. code:: shell

  lxc-attach --name="container_name" -- command

Stop
====

.. code:: shell

  lxc-stop -n "container_name"

.. code:: shell

  lxc-stop --name="container_name"

Backup
======

system
------

.. code:: shell

  cd containers/directory
  tar --numeric-owner -cvaf container_name.backup_name.txz container_name

data
----

.. code:: shell

  cd data/directory
  tar --numeric-owner -cvaf container_name.backup_name.txz container_name

Destroy
=======

.. code:: shell

  lxc-destroy -n "container_name"

.. code:: shell

  lxc-destroy --name="container_name"

Restore
=======

system
------

.. code:: shell

  cd containers/directory
  rm --recursive container_name
  tar --numeric-owner -xvf container_name.backup_name.txz

data
----

.. code:: shell

  cd data/directory
  rm --recursive container_name
  tar --numeric-owner -xvf container_name.backup_name.txz
