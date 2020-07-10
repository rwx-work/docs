Tasks
=====

* latest

  * openssl pkcs12 -nocerts -nodes -in input.p12 -out output.pem
  * openssl pkcs12 -nokeys -in input.p12 -out output.crt
  * (openssl pkcs12 -nokeys -cacerts -in input.p12 -out output.crt)
  * (openssl pkcs12 -nokeys -clcerts -in input.p12 -out output.crt)
  * ffmpeg -i input.mkv -filter:v "setpts=0.5*PTS" output.mkv
  * ffmpeg -i input.mkv -r 16 -filter:v "setpts=0.25*PTS" output.mkv
  * ffmpeg -i input.mkv -filter:a "atempo=2.0,atempo=2.0" -vn output.mkv
  * ffmpeg -i input.mkv -filter_complex "[0:v]setpts=0.5*PTS[v];[0:a]atempo=2.0[a]" -map "[v]" -map "[a]" output.mkv
  * ssh -n -N -T -R remote_port:localhost:local_port domain.tld
  * gotty
  * buster noise alsa unmute mic
  * rdesktop
  * youtube-dl -f bestaudio --extract-audio
  * /etc/bash.bashrc ← HISTTIMEFORMAT="%Y%m%d-%H%M%S "
  * fcgiwrap for git over http and gitweb
  * file
  * .git/description (gitweb)
  * peek
  * tty size → setfont (/usr/share/consolefonts/\*.psf.gz)
  * vcard spec
  * chntpw / reged -e
  * chvt
  * gpg edit change-usage (hidden)
  * qrencode -l L -m 1 -s 8 -t PNG -o pgp.png 'openpgp4fpr:FFIINNGGEERRPPRRIINNTT'
  * pdftk in.pdf background bg.pdf output out.pdf compress
  * JFIF removal in background PDF files
  * ghostscript -o in.img.pdf -sDEVICE=pdfwrite -dFILTERTEXT -dFILTERVECTOR in.pdf
  * ghostscript -o in.tav.pdf -sDEVICE=pdfwrite -dFILTERIMAGE in.pdf
  * chromium --ppapi-flash-path=/path/to/libpepflashplayer.so --ppapi-flash-version=32.0.0.171
  * git commit -S, tag -s, user.signingKey
  * youtube-dl -f bestvideo+bestaudio --all-subs --merge-output-format mkv url
  * grub: have a root menu in grub.cfg, otherwise escape sends to CLI
  * parted: print free, unit MB
  * pass
  * DNS override /etc/NetworkManager/NetworkManager.conf [main] dns=none
  * firefox ~/.mozilla/plugins ← libflashplayer.so
  * /etc/sysctl.conf net.ipv4.ip_forward=1 | /proc/sys/net/ipv4/ip_forward
  * /etc/network/interfaces → up command args…
  * lxc private network: reach out
    * iptables -t nat -A POSTROUTING -o br0 -s 10.0.0.0/8 -j MASQUERADE
  * lxc private network: get in
    * iptables -t nat -A PREROUTING -i br0 -p tcp --dport 2211 -j DNAT --to 10.0.1.1:22
  * hexdump -C -v file_path
  * qemu-system avoid junk like floppy: -nodefaults -vga virtio
  * xtra.squashfs empty media/data ← lib/live/mount/medium + data auto fstab
  * grub-bios-setup not functionin with boot.img in an overlay fs
  * qemu-system-x86_64 -initrd initrd.img -kernel vmlinuz -append root=/dev/sda1
  * adduser user kvm for -enable-kvm
  * qemu-img convert -p -O format input.ext output.ext
  * qemu-img create -f format -o ?
  * qemu-img create -f format name.ext [size]
  * qemu-img info name.ext
  * modprobe nbd
  * qemu-nbd -c /dev/nbd? name.ext
  * qemu-nbd -d /dev/nbd?
  * qemu-system-x86_64 -enable-kvm -display sdl -m 2048 -drive file=name.ext,if=virtio
  * sys: firmware-{misc-nonfree,netxen,realtek}
  * catimg
  * mount -t overlay overlay -o lowerdir=squashmount,upperdir=rwdir,workdir=emptydir squashfs-root
  * optipng
  * grub/efi: no biosdisk or ntldr
  * chromium as alternate browser
  * ['sphinx.ext.graphviz'] ⋅ graphviz_output_format = 'svg'
  * remove users' .bashrc files
  * deb [arch=amd64,i386] → /etc/apt/sources.list
  * /etc/localtime -> /usr/share/zoneinfo/Europe/Paris
  * /etc/timezone ← Europe/Paris
  * /usr/local/share/ca-certificates ⇒ update-ca-certificates
  * debian: buster/updates signed with archive-7 key
  * .git/config ← receive.denyCurrentBranch = updateInsted
  * python3: mutables persistent as constructors default
  * atop, jq, netcat
  * dependencies: readelf → ldd
  * DebFromScratch: tasks
  * /etc/dhcp/dhclient.conf no overwrite resolv.conf
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
