.. _grub_modules:

Modules
=======

Mandatory
---------

====== ==
normal | 
====== ==

dependencies
^^^^^^^^^^^^

======== ==
boot     | 
bufio    | 
crypto   | 
extcmd   | 
gettext  | 
terminal | 
======== ==

Useful
------

= ==
? | 
= ==

i386-pc
^^^^^^^

======== =================================
biosdisk | detect disks through bios
drivemap | map drives for windows bullshit
ntldr    | load windows bootmgr or ntldr
======== =================================

Useless
-------

========= ==
gcry_md5  | 
random    | 
videotest | 
========= ==

i386-pc
^^^^^^^

= ==
? | 
= ==

Untested
--------

= ==
? | 
= ==

i386-pc
^^^^^^^

============= ==
915resolution | 
cmosdump      | 
cmostest      | 
efiemu        | 
freedos       | 
gdb           | 
hwmatch       | 
lsapm         | 
mda_text      | 
pci           | 
plan9         | 
pxechain      | 
pxe           | 
sendkey       | 
truecrypt     | 
vbe           | 
vga           | 
vga_text      | 
============= ==


===== ==========================
date  display/set date/time
echo  display message
eval  expression evaluation
help  commands and args
sleep escape interruptible pause
test  if then else fi
true  true/false nop commands
===== ==========================

=========== ============================================
at_keyboard keyboard layouts handling for terminal_input
keylayouts  change keyboard layout
keystatus   test alt/ctrl/shift keys
read        variable until enter
=========== ============================================

====== ========
halt   shutdown
reboot restart
====== ========

========= =========================================
cpuid     check if cpu can handle 64 bit and/or PAE
lspci     list pci devices
videoinfo list video modes
========= =========================================

========== ======================================
part_gpt   guid partition table partitions scheme
part_msdos master boot record partitions scheme
========== ======================================

=========== ================================================
btrfs       | better file system
exfat       | ms extended file allocation table file system
ext2        | linux file systems
fat         | ms file allocation table file system
hfs         | apple file system
hfspluscomp | apple extended file system with compression
iso9660     | older optical disk file system
ntfscomp    | ms new technology file system with compression
tar         | tar archive format handling
            | (for embedded fonts,locales,etc.)
udf         | optical disk file system
=========== ================================================

====== =====================================
search set root according to uuid/label/file
====== =====================================

=========== ===================================
cat         display file content
configfile  load different menu/script file
gcry_crc    crc hash algorithm
gcry_sha1   sha1 hash algorithm
gcry_sha256 sha256 hash algorithm
gcry_sha512 sha512 hash algorithm
hashsum     hash file, needs gcry\_ modules
loadenv     load and save menu environment file
testspeed   file loading benchmark
=========== ===================================

======== =================================
loopback turn a file into a virtual device
memdisk  ram disk
======== =================================

===== =========================
linux kernel & initial ram disk
===== =========================

================== ===========================
gfxterm_background | color/image
                   | triggers graphic terminal
jpeg               | jpeg image format
png                | png image format
tga                | tga image format
================== ===========================
