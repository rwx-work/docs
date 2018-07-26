*********
Configure
*********

Keys
====

.. code:: shell

  apt-key add "path/to/key/file"

Configuration
=============

* etc/apt/apt.conf

::

  APT::Get::Show-Versions true;
  Dpkg::Progress-Fancy true;

  Acquire::Check-Valid-Until false;

* etc/apt/preferences

::

  Package: *
  Pin: release n=stretch-backports
  Pin-Priority: 400

  Package: *
  Pin: release n=buster
  Pin-Priority: 200

  Package: *
  Pin: release n=sid
  Pin-Priority: 100

* etc/apt/sources.list

.. todo::

 deb.debian.org ↔ ftp.cc.debian.org

::

  deb [arch=amd64,i386] https://deb.debian.org/debian stretch main contrib non-free
  deb [arch=amd64,i386] https://deb.debian.org/debian stretch-backports main contrib non-free
  deb [arch=amd64,i386] https://deb.debian.org/debian stretch-updates main contrib non-free
  deb [arch=amd64,i386] https://deb.debian.org/debian-security stretch/updates main contrib non-free

  deb [arch=amd64,i386] https://deb.debian.org/debian buster main contrib non-free
  deb [arch=amd64,i386] https://deb.debian.org/debian-security buster/updates main contrib non-free

  deb [arch=amd64,i386] https://deb.debian.org/debian sid main contrib non-free

.. warning::

 apt's file protocol handling fails with locations containing spaces

::

  deb file:/media/deb.debian.org/debian stretch main contrib non-free
