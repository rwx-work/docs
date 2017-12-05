**********
Standalone
**********

# Choisir les modules à inclure

[Parmi la liste suivante](modules.md)

# Télécharger les paquets nécessaires

## actuels

================== ===================================
grub2-common       fichiers v2 communs
grub-common        fichiers v2 et v1 communs
grub-efi-amd64     architecture EFI avec installation
grub-efi-amd64-bin architecture EFI sans installation
grub-pc            architecture BIOS avec installation
grub-pc-bin        architecture BIOS avec installation
================== ===================================

## anciens

=========== ============
grub-efi    transitional
grub-legacy maintenance
=========== ============

# Créer une arborescence autonome

boot/grub/grub.cfg

```bash
search --set --fs-uuid "YYYY-MM-DD-hh-mm-ss-cc"
```

Or at worst:

```bash
search --set --label "LA_BEL"
```

# Générer une image modulaire

/bin/tar
```bash
tar
--create
--dereference
--file='grub.tar'
--verbose
boot
```

* moddep.lst
* kernel.img
* lzma_decompress.img
* diskboot.img
* *.mod

/usr/bin/grub-mkimage
```bash
grub-mkimage
--directory='i386-pc'
--format='i386-pc'
--memdisk='grub.tar'
--output='i386-pc/core.img'
modules…
```

i386-pc-eltorito for ISO encapsulation

# Rendre un périphérique amorçable

* boot.img
* core.img

/usr/sbin/grub-bios-setup
```bash
grub-bios-setup \
--directory="i386-pc" \
/dev/sd?
```

# Créer un menu de démarrage

## couleurs disponibles

========= ============= =========== ==========
black     blue          green       cyan
red       magenta       brown       light-gray
dark-gray light-blue    light-green light-cyan
light-red light-magenta yellow      white
========= ============= =========== ==========

les arrière-plans noirs sont en fait transparents !

## variables d’environnement disponibles

==================== ========================================
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
prefix               (hd?,msdos?)/Portable/Grub/Versions/grub
root                 hd?,msdos?
theme                …/.txt
timeout              -1
==================== ========================================

======= =====
cmdpath (hd?)
======= =====

## fichier de persistence d’environnement

/usr/bin/grub-editenv
```bash
grub-editenv file create
grub-editenv file set variable=value
grub-editenv file unset variable
```

## démarrer un système préparé

Attention, lamentables plantages en vue si :

* le live-media-path ne comprend aucun fichier .squashfs
* le nom du fichier à charger ne finit pas par .squashfs
* le nom du fichier à charger n’est que .squashfs
* le nom du fichier à charger contient une virgule

---

* /live/name.squashfs

```bash
linux /live/subdir/vmlinuz boot="live" toram="subdir/name.squashfs"
initrd /live/subdir/initrd.img
```

```bash
loopback loop /live/dir/name.squashfs
linux (loop)/vmlinuz boot="live" toram="dir/name.squashfs"
initrd (loop)/initrd.img
```

* Debian installed

```bash
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
```

* Debian Installer

```bash
linux "/path/to/vmlinuz" priority="low"
```

```bash
linux "/path/to/vmlinuz" auto="true" \
file="/hd-media/path/to/preseed"
```

---

```bash
initrd /path/to/gtk/initrd.gz
```

---

La recherche d’ISO ne va pas à plus d’1 niveau d’arborescence !

Peut-on vraiment spécifier quelle ISO au préalable ?!

```bash
iso-scan/ask_second_pass="true" iso-scan/filename="/path/to/file.iso"
```

* Debian Live

```bash
file="/path/to.iso"
loopback loop "${file}"
path="(loop)/live"
linux "${path}/vmlinuz" boot="live" findiso="${file}" components
initrd "${path}/initrd.img"
```

* PartedMagic

```bash
file="/path/to.iso"
loopback loop ${file}
path="(loop)/pmagic"
linux "${path}/bzImage64" iso_filename="${file}" load_ramdisk=1
initrd "${path}/initrd.img" "${path}/fu.img" "${path}/m64.img"
```

* Windows

```
menuentry "Windows" {
    drivemap -s (hd0) (hd1)
    chainloader (hd0,msdos2)+1
}
```

* CloneZilla

```bash
file="/path/to/file.iso"
loopback loop "${file}"
path="(loop)/live"
linux "${path}/vmlinuz" findiso="${file}" \
boot="live" union="overlay" \
username="user" config components \
toram="filesystem.squashfs" ip="" \
locales="en_US.UTF-8" keyboard-layouts="fr-latin9" \
```

---

```bash
ocs_live_batch="yes" \
ocs_prerun="mount /dev/disk/by-uuid/${cz_home} /mnt" \
ocs_prerun1="mount --bind /mnt/${cz_partimag} /home/partimag" \
ocs_live_run="ocs-live-restore" \
```

```bash
ocs_live_extra_param="\
-e1 auto -e2 -t -r -j2 -cs -k \
-p reboot restoreparts ask_user ${cz_target}"
```

```bash
ocs_live_extra_param="\
-q2 -j2 -rm-win-swap-hib -gs -z1p -i 1000000 -fsck-y \
-p reboot saveparts ask_user ${cz_target}"
```

---

```bash
ocs_live_batch="no" \
ocs_live_run="ocs-live-general" \
```

---

```bash
initrd "${path}/initrd.img"
```

* ISO

```bash
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
```
