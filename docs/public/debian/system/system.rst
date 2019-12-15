.. todo::

 * /etc/motd

Choices
=======

have up-to-date mirrors available
---------------------------------

.. todo:: sync mirrors
.. todo:: check mirrors

critical base packages
----------------------

 +-----------+--------------------------------------------------+
 | locales   | to get localization binaries for system messages |
 +-----------+--------------------------------------------------+
 | apt-utils | otherwise packages configuration gets delayed    |
 +-----------+--------------------------------------------------+
 | dialog    | to have user interaction possible with APT       |
 +-----------+--------------------------------------------------+

decide the desired type of system
---------------------------------

 * will the system run
   * 64 bits?
   * 32 bits?
   * both?
 * will the system be run by
   * a physical machine?
   * a virtual machine?
   * a container?
   * a container inside a virtual machine?
 * will the system be stored
   * read-write, as a file system on a dedicated partition?
   * read-only, as a single file loaded in RAM at boot time?

Install required tools
======================

 ============== ========================================
 debootstrap    generate a minimal base file system
 squashfs-tools archive or unarchive a file system image
 ============== ========================================

 .. code:: shell

  apt install debootstrap squashfs-tools

Create a base file hierarchy
============================

prepare the system's directory
------------------------------

* become root
* make a directory and step into it

.. code:: shell

 su

.. code:: shell

 mkdir -p "path"
 cd "path"

generate the minimal base
-------------------------

.. code:: shell

 debootstrap \
 --arch="amd64" \
 --include="locales,apt-utils,dialog" \
 --variant="minbase" \
 "stretch" \
 . \
 "miroir"

Configure preinstalled packages
===============================

define default keyboard layouts
-------------------------------

* /etc/default/keyboard

::

 XKBMODEL="pc105"
 XKBLAYOUT="fr,fr"
 XKBVARIANT="oss,bepo"
 XKBOPTIONS=""
 BACKSPACE="guess"

define default locales to generate
----------------------------------

* etc/default/locale

::

 LANG=en_US.UTF-8
 LANGUAGE=en_US:en
 LC_CTYPE="fr_FR.UTF-8"
 LC_NUMERIC="fr_FR.UTF-8"
 LC_TIME="fr_FR.UTF-8"
 LC_COLLATE="fr_FR.UTF-8"
 LC_MONETARY="fr_FR.UTF-8"
 LC_MESSAGES="en_US.UTF-8"
 LC_PAPER="fr_FR.UTF-8"
 LC_NAME="fr_FR.UTF-8"
 LC_ADDRESS="fr_FR.UTF-8"
 LC_TELEPHONE="fr_FR.UTF-8"
 LC_MEASUREMENT="fr_FR.UTF-8"
 LC_IDENTIFICATION="fr_FR.UTF-8"

* etc/locale.gen

::

 en_US.UTF-8 UTF-8
 fr_FR.UTF-8 UTF-8

[configure command shell](../bash/index.md)
-------------------------------------------

[configure package manager](../apt/index.md)
--------------------------------------------

redefine hostname
-----------------

.. code:: shell

 echo "hostname" > "etc/hostname"

provide known file systems
--------------------------

* etc/fstab

Volume temporaire en RAM

::

 tmpfs /tmp tmpfs auto,mode=1777 0 0

Install additional packages
===========================

switch into context
-------------------

.. code:: shell

 mount --bind /proc proc
 mount --bind /sys sys
 chroot .

.. todo:: /dev

generate locales
----------------

.. code:: shell

 locale-gen

define root password
--------------------

.. code:: shell

 passwd

user, guest, sudo
-----------------

.. code:: shell

 apt-get install sudo

 useradd -s /bin/bash user
 mkdir /home/user
 chown user: /home/user
 adduser user sudo

 useradd -s /bin/bash guest
 chown guest: /home/guest

authentications: passwords, SSH keys
------------------------------------

.. todo:: files

upgrade system
--------------

* dans tous les cas :

.. code:: shell

 apt-get update
 apt-get upgrade

* si besoin, car des paquets rétroportés modifient la distribution :

.. code:: shell

 apt-get dist-upgrade

apply system type elements
--------------------------

================= ==================================================
linux-image-amd64 s’il ne s’agit pas d’un conteneur
live-boot         si à destination de boot live
systemd-sysv      sans quoi le système ne démarrera pas complètement
================= ==================================================

.. code:: shell

 apt-get install -t stretch-backports "linux-image-amd64"
 apt-get install "live-boot"

----

initialization settings
-----------------------

.. code:: shell

 apt-get install -t stretch-backports "systemd-sysv"

* etc/sysctl.conf

Espace mémoire maximum allouable (à augmenter si hébergement de conteneurs)  
Pourcentage de RAM disponible avant utilisation de la partition d’échange  

.. code:: ini

 vm.max_map_count=1048576
 vm.swappiness=0

keeping things light
--------------------

.. code:: shell

 apt-get install --no-install-recommends …

install useful packages
-----------------------

.. code:: shell

 apt-get install \
 bash-completion \
 lxc \
 less nano vim \
 pciutils usbutils \
 python3 \
 squashfs-tools \

.. code:: shell

 apt-get install -t "stretch-backports" \
 debootstrap \

install other packages
----------------------

[Choix de paquets commentés](packages.md)

.. code:: shell

 apt-get install "package1" …
 apt-get install -t stretch-backports "package1" …

properly switch back from context
---------------------------------

* vider le cache d’APT

.. code:: shell

 apt-get clean

* s’extraire de l’environnement

.. code:: shell

 exit

* démonter les liens au système hôte

.. code:: shell

 umount sys
 umount proc

clean up commands history
-------------------------

* root/.bash_history

Configure installed packages
============================

.. todo:: files

Archive prepared file system
============================

.. code:: shell

  mksquashfs . "../name.squashfs" -comp "xz"
