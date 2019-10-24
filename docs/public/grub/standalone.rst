************************
Prepare a boot directory
************************

Choose useful modules
=====================

Commented list: :ref:`grub_modules`

Download packages
=================

current
-------

================== ===================================
grub2-common       fichiers v2 communs
grub-common        fichiers v2 et v1 communs
grub-efi-amd64     architecture EFI avec installation
grub-efi-amd64-bin architecture EFI sans installation
grub-pc            architecture BIOS avec installation
grub-pc-bin        architecture BIOS avec installation
================== ===================================

legacy
------

=========== ============
grub-efi    transitional
grub-legacy maintenance
=========== ============

Put up a functional directory
=============================

boot/grub/grub.cfg

.. code:: shell

  search --set --fs-uuid "YYYY-MM-DD-hh-mm-ss-cc"

Or at worst:

.. code:: shell

  search --set --label "LA_BEL"

Generate a modular image
========================

/bin/tar

.. code:: shell

  tar
  --create
  --dereference
  --file='grub.tar'
  --verbose
  boot

* moddep.lst
* kernel.img
* lzma_decompress.img
* diskboot.img
* \*.mod

/usr/bin/grub-mkimage

.. code:: shell

  grub-mkimage
  --directory='i386-pc'
  --format='i386-pc'
  --memdisk='grub.tar'
  --output='i386-pc/core.img'
  modules…

i386-pc-eltorito for ISO encapsulation

Make a device bootable
======================

* boot.img
* core.img

/usr/sbin/grub-bios-setup

.. code:: shell

  grub-bios-setup \
  --directory="i386-pc" \
  /dev/sd?

Prepare a boot menu
===================

available colors
----------------

========= ============= =========== ==========
black     blue          green       cyan
red       magenta       brown       light-gray
dark-gray light-blue    light-green light-cyan
light-red light-magenta yellow      white
========= ============= =========== ==========

* black backgrounds are actually transparent!

available environment variables
-------------------------------

==================== =============================
chosen               4
color_highlight      black/light-gray
color_normal         light-gray/black
default              "${id}"
gfxmode              1024x768
gfxpayload           keep
gfxterm_font         unicode
lang                 en_US
locale_dir
menu_color_highlight white/blue
menu_color_normal    cyan/blue
pager                1
prefix               (hd?,msdos?)/live/boot/2.02-2
root                 hd?,msdos?
theme                …/.txt
timeout              -1
==================== =============================

======= =====
cmdpath (hd?)
======= =====

persistent environment variables file
-------------------------------------

* /usr/bin/grub-editenv

.. code:: shell

  grub-editenv file create
  grub-editenv file set variable=value
  grub-editenv file unset variable

boot a prepared system
----------------------

.. warning::

  Violent kernel crashes are to be expected if:

  1. the live-media-path has no .squashfs file
  #. the image basename:

     * doesn't end with .squashfs
     * is just .squashfs
     * contains ,

----

* /live/name.squashfs

.. code:: shell

  linux /live/subdir/vmlinuz boot="live" toram="subdir/name.squashfs"
  initrd /live/subdir/initrd.img

.. code:: shell

  loopback loop /live/dir/name.squashfs
  linux (loop)/vmlinuz boot="live" toram="dir/name.squashfs"
  initrd (loop)/initrd.img

* Debian installed

.. code:: shell

  unset path
  uuid="????????-????-????-????-????????????"
  search --set="path" --fs-uuid "${uuid}"
  if [ "${path}" ]; then
      path="(${path})"
      linux "${path}/vmlinuz" \
          elevator=deadline \
          root=UUID=${uuid}
      initrd "${path}/initrd.img"
  fi

* Debian Installer

.. code:: shell

  linux "/path/to/vmlinuz" priority="low"

.. code:: shell

  linux "/path/to/vmlinuz" auto="true" \
  file="/hd-media/path/to/preseed"

----

.. code:: shell

  initrd /path/to/gtk/initrd.gz

----

* iso-scan's first pass goes only 1 subdirectories level down!

.. todo::

  Test if iso-scan/filename really works

.. code:: shell

  iso-scan/ask_second_pass="true" iso-scan/filename="/path/to/file.iso"

* Debian Live

.. code:: shell

  file="/path/to.iso"
  loopback loop "${file}"
  path="(loop)/live"
  linux "${path}/vmlinuz" boot="live" findiso="${file}" components
  initrd "${path}/initrd.img"

* PartedMagic

.. code:: shell

  file="/path/to.iso"
  loopback loop ${file}
  path="(loop)/pmagic"
  linux "${path}/bzImage64" iso_filename="${file}" load_ramdisk=1
  initrd "${path}/initrd.img" "${path}/fu.img" "${path}/m64.img"

* Windows ≥ Vista

.. code:: shell

  menuentry "Windows" {
      root=(hd0,msdos2)
      ntldr /bootmgr
  }

* Windows ≤ XP

.. code:: shell

  menuentry "Windows" {
      drivemap -s (hd0) (hd1)
      chainloader (hd0,msdos2)+1
  }

* CloneZilla

.. code:: shell

  file="/path/to/file.iso"
  loopback loop "${file}"
  path="(loop)/live"
  linux "${path}/vmlinuz" findiso="${file}" \
  boot="live" union="overlay" \
  username="user" config components \
  toram="filesystem.squashfs" ip="" \
  locales="en_US.UTF-8" keyboard-layouts="fr-latin9" \

----

.. code:: shell

  ocs_live_batch="yes" \
  ocs_prerun="mount /dev/disk/by-uuid/${cz_home} /mnt" \
  ocs_prerun1="mount --bind /mnt/${cz_partimag} /home/partimag" \
  ocs_live_run="ocs-live-restore" \

.. code:: shell

  ocs_live_extra_param="\
  -e1 auto -e2 -t -r -j2 -cs -k \
  -p reboot restoreparts ask_user ${cz_target}"

.. code:: shell

  ocs_live_extra_param="\
  -q2 -j2 -rm-win-swap-hib -gs -z1p -i 1000000 -fsck-y \
  -p reboot saveparts ask_user ${cz_target}"

----

.. code:: shell

  ocs_live_batch="no" \
  ocs_live_run="ocs-live-general" \

----

.. code:: shell

  initrd "${path}/initrd.img"

* ISO

.. code:: shell

  xorrisofs \
  \
  -output live-grub.iso \
  \
  -volid "LIVE_GRUB" \
  -boot-info-table \
  -no-emul-boot \
  --modification-date="YYYYMMDDhhmmsscc" \
  -eltorito-boot live/boot/grub/2.02-2/i386-pc/core.img \
  -eltorito-catalog "boot.cat" \
  --boot-catalog-hide \
  \
  -exclude live/sources \
  -exclude live/boot/debian.squashfs/debootstrap \
  -exclude live/boot/debian.squashfs/live \
  -root "live" \
  "live"
