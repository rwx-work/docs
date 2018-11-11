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
usbtest   | 
videoinfo | 
========= ==

part
^^^^

========== ==
lvm        | 
mdraid1x   | 
part_bsd   | 
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
gcry_md5     | 
mdraid09     | 
mdraid09_be  | 
random       | 
tga          | 
time         | 
usb_keyboard | 
videotest    | 
============ ==

i386-pc
^^^^^^^

= ==
? | 
= ==

Untested
--------

==================== ==

acpi
adler32
affs
afs
ahci
all_video
aout
archelp
ata
at_keyboard
backtrace
bfs
bitmap
bitmap_scale
blocklist
boot
bsd
bswap_test
btrfs
bufio
cat
cbfs
cbls
cbmemc
cbtable
cbtime
chain
cmdline_cat_test
cmp
cmp_test
configfile
cpio_be
cpio
cpuid
crc64
cryptodisk
crypto
cs5536
ctz_test
datehook
date
datetime
diskfilter
disk
div
div_test
dm_nv
echo
ehci
elf
eval
exfat
exfctest
ext2
extcmd
fat
file
font
fshelp
functional_test
gcry_arcfour
gcry_blowfish
gcry_camellia
gcry_cast5
gcry_crc
gcry_des
gcry_dsa
gcry_idea
gcry_md4
gcry_md5
gcry_rfc2268
gcry_rijndael
gcry_rmd160
gcry_rsa
gcry_seed
gcry_serpent
gcry_sha1
gcry_sha256
gcry_sha512
gcry_tiger
gcry_twofish
gcry_whirlpool
geli
gettext
gfxmenu
gfxterm_background
gfxterm_menu
gfxterm
gptsync
gzio
halt
hashsum
hdparm
hello
help
hexdump
hfs
hfspluscomp
hfsplus
http
iorw
iso9660
jfs
jpeg
keylayouts
keystatus
ldm
legacycfg
legacy_password_test
linux16
linux
loadenv
loopback
lsacpi
lsmmap
ls
lspci
luks
lvm
lzopio
macbless
macho
mdraid09_be
mdraid09
mdraid1x
memdisk
memrw
minicmd
minix2_be
minix2
minix3_be
minix3
minix_be
minix
mmap
morse
mpi
msdospart
mul_test
multiboot2
multiboot
nativedisk
net
newc
nilfs2
normal
ntfscomp
ntfs
odc
offsetio
ohci
part_acorn
part_amiga
part_apple
part_bsd
part_dfly
part_dvh
part_gpt
part_msdos
part_plan
part_sun
part_sunpc
parttool
password
password_pbkdf2
pata
pbkdf2
pbkdf2_test
pcidump
play
png
priority_queue
probe
procfs
progress
raid5rec
raid6rec
random
read
reboot
regexp
reiserfs
relocator
romfs
scsi
search_fs_file
search_fs_uuid
search_label
search
serial
setjmp
setjmp_test
setpci
sfs
shift_test
signature_test
sleep
sleep_test
spkmodem
squash4
syslinuxcfg
tar
terminal
terminfo
test_blockarg
testload
test
testspeed
tftp
tga
time
trig
tr
true
udf
ufs1_be
ufs1
ufs2
uhci
usb_keyboard
usb
usbms
usbserial_common
usbserial_ftdi
usbserial_pl2303
usbserial_usbdebug
usbtest
verify
video_bochs
video_cirrus
video_colors
video_fb
videoinfo
video
videotest_checksum
videotest
xfs
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
