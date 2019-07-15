Server
======

Hardware
--------

=== ================================
BHS KS-12
CPU Intel Xeon W3530 4c/8t @ 2.8 GHz
RAM 32 GB DDR3 ECC @ 1333 MHz
HDD 2 × 2 TB
WAN 100 Mbps /128
IP4 192.99.14.98
IP6 2607:5300:60:3f62::1
=== ================================

Rescue
------

.. code:: shell

 ssh-keygen -f /home/user/.ssh/known_hosts -R rwx.work
 ssh-keygen -f /home/user/.ssh/known_hosts -R 192.99.14.98
 scp /home/user/.ssh/id_ecdsa.pub root@rwx.work:/root/.ssh/authorized_keys
 scp /etc/bash.bashrc root@rwx.work:/etc/

Partitions
----------

.. code:: shell

 parted

 select /dev/sda
 mktable gpt
 mkpart boot 1 2
 mkpart raid 2 2000399
 toggle 1 bios_grub

 select /dev/sdb
 mktable gpt
 mkpart boot 1 2
 mkpart raid 2 2000399
 toggle 1 bios_grub

 q

.. code:: shell

 mdadm --create /dev/md0 \
 --level 0 --raid-devices 2 /dev/sd[ab]2

.. code:: shell

 parted /dev/md0

 mktable gpt
 mkpart data 1 3966966
 mkpart swap 3966966 4000523

 q

.. code:: shell

 mkswap --label swap \
 -U d8ee4260-4652-7192-7bb3-ebbadeb835a7 \
 /dev/md0p2
 mkfs.ext4 -L data \
 -U 46527192-7bb3-ebba-deb8-35a7e8606808 \
 /dev/md0p1

Boot
----

.. warning:: no ESP boot available!

Prepare a grub.cfg

.. code:: shell

 insmod biosdisk
 insmod part_gpt
 insmod mdraid1x
 insmod ext2
 insmod search
 insmod squash4
 insmod loopback
 insmod linux

 search --set data --fs-uuid 46527192-7bb3-ebba-deb8-35a7e8606808
 lmp=/fs/default
 sfs=filesystem.squashfs

 loopback loop (${data})${lmp}/${sfs}

 linux (loop)/vmlinuz \
 boot=live \
 elevator=deadline \
 ip=frommedia \
 live-media-path=${lmp} \
 toram=${sfs}

 initrd (loop)/initrd.img

 boot

.. code:: shell

 grub-mkstandalone \
 --verbose \
 --compress xz \
 --format i386-pc \
 --output core.img \
 --themes "" \
 boot/grub/grub.cfg=grub.cfg \
 --fonts "" \
 --locales "" \
 --install-modules "\
 biosdisk \
 part_gpt \
 mdraid1x \
 ext2 \
 search \
 squash4 \
 loopback \
 linux \
 "

Maybe one day:

.. code:: shell

 grub-mkstandalone \
 --verbose \
 --compress xz \
 --format x86_64-efi \
 --output bootx64.efi \
 --themes "" \
 boot/grub/grub.cfg=grub.cfg

.. code:: shell

 scp core.img root@rwx.work:
 cp /usr/lib/grub/i386-pc/boot.img . \
 /usr/lib/grub/i386-pc/grub-bios-setup \
 --directory . /dev/sda
 /usr/lib/grub/i386-pc/grub-bios-setup \
 --directory . /dev/sdb

* /etc/locale.gen
* locale-gen
* /etc/resolv.conf
* /etc/apt/sources.list
* apt update
* apt upgrade
* apt install openssh-server
* apt clean
* /etc/ssh/sshd_config
* mkdir /root/.ssh
* echo "ecdsa-sha2-nistp521 AAAAE2VjZHNhLXNoYTItbmlzdHA1MjEAAAAIbmlzdHA1MjEAAACFBAFBp8vFUIRu4Bq8EvnCGwlp71GQ4wGT5wKdY1X/c9AfYjsn/pnBNgnfNFxPxoNasG1MXeXjutSLtlXqnsWx2NQpFQC321MeUvd3Z/DCeIvS4WvpOZMyBvVUd2sTsuuCRVuH3fbJF5XPJrFzH3nEFNtcW7lmN+F6nKLB0kYahc3+gyTH+g==" > /root/.ssh/authorized_keys
* /etc/network/interfaces.d/setup

.. warning:: inet6 dhcp hangs!

::

 auto  lo
 iface lo inet loopback
 iface lo inet6 loopback

 auto  enp1s0
 iface enp1s0 inet static
       address 192.99.14.98/24
       gateway 192.99.14.254
 iface enp1s0 inet static
       address 10.0.0.254/24
 iface enp1s0 inet6 static
       address 2607:5300:60:3f62::1/64
       gateway 2607:5300:60:3fff:ff:ff:ff:ff
