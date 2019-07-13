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

Partitions
----------

.. code:: shell

 parted

 select /dev/sda
 mktable gpt
 mkpart raid 1 2000364
 mkpart boot 2000364 2000399
 toggle 2 boot

 select /dev/sdb
 mktable gpt
 mkpart raid 1 2000364
 mkpart boot 2000364 2000399
 toggle 2 boot

 q

.. code:: shell

 mdadm --create /dev/md0 \
 --level 0 --raid-devices 2 /dev/sd[ab]1

.. code:: shell

 parted /dev/md0

 mktable gpt
 mkpart data 1 3966099
 mkpart swap 3966099 4000458

 q

.. code:: shell

 mkfs.ext4 -L data /dev/md0p1
 mkswap --label swap /dev/md0p2
 mkfs.vfat -n boot /dev/sda2
 mkfs.vfat -n boot /dev/sdb2

.. code:: shell

 cd /mnt
 mkdir a2 b2
 mount /dev/sda2 a2
 mount /dev/sdb2 b2
 mkdir --parents a2/efi/boot
 mkdir --parents b2/efi/boot

Boot
----

Prepare a grub.cfg

.. code:: shell

 insmod part_gpt
 insmod mdraid1x
 insmod ext2
 insmod search
 insmod squash4
 insmod loopback
 insmod linux

 search --set data --fs-uuid f3eefba5-1f22-4651-bf60-72ec21ec9e30
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

.. code:: shell

 grub-mkstandalone \
 --verbose \
 --compress xz \
 --format x86_64-efi \
 --output bootx64.efi \
 --themes "" \
 boot/grub/grub.cfg=grub.cfg

.. code:: shell

 scp bootx64.efi root@rwx.work:/mnt/a2/efi/boot/
 scp bootx64.efi root@rwx.work:/mnt/b2/efi/boot/

* /etc/locale.gen
* locale-gen
* /etc/resolv.conf
* apt update
* apt upgrade
* apt install openssh-server
* apt clean
* /etc/ssh/sshd_config
* mkdir /root/.ssh
* echo "ecdsa-sha2-nistp521 AAAAE2VjZHNhLXNoYTItbmlzdHA1MjEAAAAIbmlzdHA1MjEAAACFBAFBp8vFUIRu4Bq8EvnCGwlp71GQ4wGT5wKdY1X/c9AfYjsn/pnBNgnfNFxPxoNasG1MXeXjutSLtlXqnsWx2NQpFQC321MeUvd3Z/DCeIvS4WvpOZMyBvVUd2sTsuuCRVuH3fbJF5XPJrFzH3nEFNtcW7lmN+F6nKLB0kYahc3+gyTH+g==" > /root/.ssh/authorized_keys
