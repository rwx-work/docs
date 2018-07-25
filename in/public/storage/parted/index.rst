Parted
======

Examples with 2 × 2 TB hard disk drives as MBR,
for a virtual 4 TB with data and 32 GB of swap as GPT.

MBR
---

::

 parted /dev/sda
 mktable msdos
 mkpart primary 1 2000399

::

 parted /dev/sdb
 mktable msdos
 mkpart primary 1 2000399

.. warning::

 The first megabyte makes room for an embedded bootloader.

GPT
---

::

 parted /dev/md0
 mktable gpt
 mkpart data 1 3966128
 mkpart swap 2 4000527

.. info::

 Start offset of a partition can be inferior than actual free space beginning.
