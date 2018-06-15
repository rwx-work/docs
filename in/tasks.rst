#####
Tasks
#####

* latest

  * Dir::Etc::sourceparts "";
  * Acquire::Check-Valid-Unitl false;
  * APT::Install-Recommends "false";
  * APT::Install-Suggests "false";
  * debootstrap: minbase
  * debootstrap: umount machine-id afterwards
  * machine-id: /etc empty ⋅ /var/lib/dbus useless
  * DEBIAN_FRONTEND="noninteractive" for apt install
  * console-setup -> /etc/default/keyboard
  * console-data -> loadkeys fr
  * org.gnome.desktop.media-handling.autorun-never true
  * org.gnome.desktop.interface.text-scaling-factor 1.5
  * AppArmor/lxc? lxc.aa_profile = unconfined
  * graphviz
  * tig
  * upx-ucl
  * ?/vmlinuz apparmor=0 (KO backports profiles)
  * LD_LIBRARY_PATH=path/to/libs path/to/executable
  * upx --best executable
  * nuitka --portable --python-version=3.5 --remove-output --show-progress --show-modules main.py
  * bpython3
  * sphinx configuration
  * __git_complete gco _git_checkout
  * git LFS
  * apt-mirror
  * DEBIAN_FRONTEND=noninteractive for keyboard-configuration interactive prompt
  * sudo, sudoers
  * sqlite
  * umask
  * node, process.umask(2)

* critical

    * ~/.config/gtk-3.0 → bookmarks ⋅ settings.ini
    * dbus-run-session -- gsettings set key value
    * gsettings get key
    * linux: ram merges live-media-path's squashfs files but not fully in RAM
    * linux: toram=xxx.squashfs
    * ram disk size argument
    * panic kernel argument for seconds to automatically reboot
    * ! manual build of live-boot system's initrd.img after kernel upgrade

    * /etc/skel
    * auto-update if firefox archive in ~/.local

    * ? systemd-sysv ↔ linux-image-amd64 ↔ live-boot
    * ! GUI keyboard-configuration /etc/default/keyboard

    * reference missing mkdocs strict option

    * apt-transport-https
    * dhcpcd

    * handle upstream GPG public keys
    * check authenticity mirrors with GPG

    * lxc-create packages

      * ${init}
      * ifupdown
      * locales
      * dialog
      * isc-dhcp-client
      * netbase
      * net-tools
      * iproute
      * openssh-server

* extra

    * json.load(f, object_pairs_hook=collections.OrderedDict)
    * tty screenshot → sudo fbcat > name.ppm
    * consoleblank=0 / setterm --blank 0
    * on-the-fly LibreOffice documents conversion
    * send emails as own domain name's alias
    * personal GPG key signature

Network interfaces
==================

* /etc/network/interfaces

.. code:: shell

  source /etc/network/interfaces.d/*

* /etc/network/interfaces.d/lo

::

  auto lo
  iface lo inet loopback

* /etc/network/interfaces.d/eth0

::

  auto eth0
  iface eth0 inet dhcp

Name resolution
===============

* /etc/hosts

::

  127.0.0.1 localhost

  ::1 localhost
