.. _grub_modules:

Modules
=======

Included
--------

======= ==
memdisk | 
tar     | 
======= ==

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

core
^^^^

========== ==
date       | 
echo       | 
eval       | 
help       | 
keylayouts | 
ls         | 
sleep      | 
test       | 
true       | 
========== ==

hw
^^

========= ==
cpuid     | 
lspci     | 
terminfo  | 
videoinfo | 
========= ==

part
^^^^

========== ==
lvm        | 
mdraid1x   | 
part_bsd   | 
part_dfly  | 
part_gpt   | 
part_msdos | 
raid5rec   | 
========== ==

fs
^^

=========== ==
btrfs       | 
exfat       | 
ext2        | 
fat         | 
hfs         | 
hfspluscomp | 
iso9660     | 
ntfscomp    | 
squash4     | 
udf         | 
xfs         | 
zfs         | 
=========== ==

file
^^^^

======== ==
cat      | 
cmp      | 
file     | 
hexdump  | 
loadenv  | 
loopback | 
probe    | 
regexp   | 
search   | 
======== ==

hash
^^^^

=========== ==
hashsum     | 
gcry_sha1   | 
gcry_sha256 | 
gcry_sha512 | 
=========== ==

action
^^^^^^

========== ==
bsd        | 
configfile | 
halt       | 
keystatus  | 
linux      | 
read       | 
reboot     | 
========== ==

gfx
^^^

================== ==
gfxterm_background | 
jpeg               | 
png                | 
================== ==

bench
^^^^^

========= ==
progress  | 
testspeed | 
========= ==

i386-pc
^^^^^^^

======== =================================
biosdisk | detect disks through bios
drivemap | map drives for windows bullshit
ntldr    | load windows bootmgr or ntldr
======== =================================

Useless
-------

============ ==
at_keyboard  | 
gcry_crc     | 
gcry_md4     | 
gcry_md5     | 
mdraid09     | 
mdraid09_be  | 
random       | 
tga          | 
time         | 
usb_keyboard | 
usbtest      | 
videotest    | 
============ ==

i386-pc
^^^^^^^

= ==
? | 
= ==

Untested
--------

========== ==
part_acorn | 
part_amiga | 
part_apple | 
part_dvh   | 
part_plan  | 
part_sun   | 
part_sunpc | 
========== ==

========= ==
affs      | 
afs       | 
bfs       | 
cbfs      | 
cpio      | 
cpio_be   | 
hfsplus   | 
jfs       | 
minix     | 
minix_be  | 
minix2    | 
minix2_be | 
minix3    | 
minix3_be | 
nilfs2    | 
ntfs      | 
procfs    | 
reiserfs  | 
romfs     | 
sfs       | 
ufs1      | 
ufs1_be   | 
ufs2      | 
========= ==

============== ==
adler32        | 
crc64          | 
gcry_arcfour   | 
gcry_blowfish  | 
gcry_camellia  | 
gcry_cast5     | 
gcry_des       | 
gcry_dsa       | 
gcry_idea      | 
gcry_rfc2268   | 
gcry_rijndael  | 
gcry_rmd160    | 
gcry_rsa       | 
gcry_seed      | 
gcry_serpent   | 
gcry_tiger     | 
gcry_twofish   | 
gcry_whirlpool | 
============== ==

==================== ==
acpi
ahci
all_video
aout
archelp
ata
backtrace
bitmap
bitmap_scale
blocklist
bswap_test
cbls
cbmemc
cbtable
cbtime
chain
cmdline_cat_test
cmp_test
cryptodisk
cs5536
ctz_test
datehook
datetime
disk
diskfilter
div
div_test
dm_nv
ehci
elf
exfctest
font
fshelp
functional_test
geli
gfxmenu
gfxterm
gfxterm_menu
gptsync
gzio
hdparm
hello
http
iorw
ldm
legacycfg
legacy_password_test
linux16
lsacpi
lsmmap
luks
lzopio
macbless
macho
memrw
minicmd
mmap
morse
mpi
msdospart
mul_test
multiboot
multiboot2
nativedisk
net
newc
odc
offsetio
ohci
parttool
password
password_pbkdf2
pata
pbkdf2
pbkdf2_test
pcidump
play
priority_queue

raid6rec
relocator
scsi
search_fs_file
search_fs_uuid
search_label
serial
setjmp
setjmp_test
setpci
shift_test
signature_test
sleep_test
spkmodem
syslinuxcfg
test_blockarg
testload
tftp
trig
tr
uhci
usb
usbms
usbserial_common
usbserial_ftdi
usbserial_pl2303
usbserial_usbdebug
verify
video_bochs
video_cirrus
video_colors
video_fb
video
videotest_checksum
xnu
xnu_uuid
xnu_uuid_test
xzio
zfscrypt
zfsinfo
zfs
==================== ==

x86_64-efi
^^^^^^^^^^

=========== ==
appleldr    | 
efifwsetup  | 
efi_gop     | 
efinet      | 
efi_uga     | 
fixvideo    | 
linuxefi    | 
loadbios    | 
lsefimmap   | 
lsefi       | 
lsefisystab | 
lssal       | 
=========== ==

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
