To dispatch
===========

Hardware
--------

=== ================================
BHS KS-12
CPU Intel Xeon W3530 4c/8t @ 2.8 GHz
RAM 32 GB DDR3 ECC @ 1333 MHz
HDD 2 × 2 TB
MAC 00:25:90:7b:d4:38
WAN 100 Mbps
=== ================================

Network
-------

+-----+---------+-------------------------------+
| IP4 | address | 192.99.14.98 /24              |
|     +---------+-------------------------------+
|     | gateway | 192.99.14.254                 |
+-----+---------+-------------------------------+
| IP6 | address | 2607:5300:60:3f62::1          |
|     +---------+-------------------------------+
|     | gateway | 2607:5300:60:3fff:ff:ff:ff:ff |
+-----+---------+-------------------------------+

Rescue
------

.. code:: shell

 ssh-keygen -R rwx.work
 ssh-keygen -R 192.99.14.98
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
 lmp=/fs/up
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

.. todo:: move to public grub

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

* debootstrap
* apt
* user account and home directory
* fstab /d
* systemd
* linux-image
* tops
* hardware
* completion
* network
* interfaces
* iputils-ping
* basics
* openssh-server fixes (sshd user, /run/sshd)
* live-boot
* root
* inception
* bridge
* grub-pc-bin
* apparmor
* unbound
* tree
* net.ipv4.ip_forward=1
* net.ipv6.conf.all.forwarding=1
* nftables
* nginx-extras
* root/user authorized_keys
* curl
* swap,swappiness
* enable nftables.service
* enable lxc.service
* sources.list file:/
* syslog-ng
* ssh on port 80
* domain certificate private key
* domain certificate bundle
* /etc/ssl/openssl.cnf tls 1.3 suites
* nginx configuration
* nginx in container
* nginx host sites
* python3-sphinx-rtd-theme
* uwsgi
* uwsgi-plugin-python3
* sudo

* /etc/bash.bashrc
* /etc/fstab (/d)
* /etc/locale.gen
* locale-gen
* /etc/resolv.conf
* /etc/apt/apt.conf
* /etc/apt/sources.list
* apt update
* apt upgrade
* live-boot
* update-initramfs ← update-initramfs.orig
* openssh-server
* parted
* squashfs-tools
* tree
* apt clean
* /etc/ssh/sshd_config
* mkdir /root/.ssh
* echo "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICZAs76kQJ0/Et2NGzhxurK2wE0VhYsG9wl85iCmR9xH" > /root/.ssh/authorized_keys
* lxc
* /etc/network/interfaces.d/setup

.. warning:: inet6 dhcp hangs!

::

 auto  lo
 iface lo inet loopback
 iface lo inet6 loopback

 auto  br0
 iface br0 inet static
       address 10.0.0.254/24
       bridge_fd 0
       bridge_maxwait 0
       bridge_ports enp1s0
       bridge_stp on
 iface br0 inet static
       address 192.99.14.98/24
       gateway 192.99.14.254
 iface br0 inet6 static
       address 2607:5300:60:3f62::1/64
       gateway 2607:5300:60:3fff:ff:ff:ff:ff

.. warning::

 reboot from container doesn't reload config file

/var/lib/lxc/config

::

 lxc.include = /usr/share/lxc/config/common.conf
 lxc.mount.entry = /d/mirrors/apt-mirror/debian deb none bind,create=dir,ro 0 0
 lxc.start.auto = 1
 lxc.net.0.type = veth
 lxc.net.0.flags = up
 lxc.net.0.link = br0

/var/lib/lxc/name/config

::

 lxc.include = /var/lib/lxc/config
 lxc.mount.entry = /d/d/buster d none bind,create=dir,rw 0 0
 lxc.rootfs.path = dir:/var/lib/lxc/buster
 lxc.net.0.veth.pair = buster
 lxc.net.0.ipv4.address = 10.0.0.1/24
 lxc.net.0.ipv4.gateway = 10.0.0.254

/etc/nftables.conf

::

 #! /usr/sbin/nft --file

 flush ruleset

 table inet filter {
     chain input {
         type filter hook input priority 0; policy accept;
         iifname "lo" accept
         ip protocol icmp accept
         ip6 nexthdr icmp accept
         tcp dport ssh accept
         tcp dport domain accept
         tcp dport http accept
         tcp dport https accept
     }
     chain forward {
         type filter hook forward priority 0; policy accept;
     }
     chain output {
         type filter hook output priority 0; policy accept;
     }
 }

 table ip nat {
     chain prerouting {
         type nat hook prerouting priority 0; policy accept;
         tcp dport 65001 dnat to 10.0.0.1:ssh
     }
     chain postrouting {
         type nat hook postrouting priority 0; policy accept;
         masquerade
     }
 }

Security
--------

* /etc/sudoers

.. todo:: all directives

::

 user ALL=NOPASSWD: /bin/systemctl restart uwsgi

Web
---

Configuration
^^^^^^^^^^^^^

* /etc/nginx/nginx.conf

::

 load_module modules/ngx_http_fancyindex_module.so;
 load_module modules/ngx_http_headers_more_filter_module.so;

 pid /run/nginx.pid;
 user user;
 worker_processes auto;

 events {
 multi_accept off;
 worker_connections 512;
 }

 http {

 # General

 keepalive_timeout 60;
 sendfile on;
 server_tokens off;
 tcp_nopush on;
 tcp_nodelay on;
 types_hash_max_size 2048;

 # Names

 server_name_in_redirect off;
 server_names_hash_bucket_size 128;

 # File types

 include mime.types;
 default_type application/octet-stream;

 # Security

 ssl_buffer_size 8k;
 ssl_ciphers "ECDHE-RSA-CHACHA20-POLY1305:ECDHE-ARIA256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384";
 ssl_ecdh_curve "X448:X25519:P-521";
 ssl_prefer_server_ciphers on;
 ssl_protocols TLSv1.3 TLSv1.2;
 ssl_session_cache shared:ssl_session_cache:16m;
 ssl_session_tickets off;
 ssl_session_timeout 15m;

 # Log

 access_log /var/log/nginx/access.log;
 error_log /var/log/nginx/error.log;

 # Compression

 gzip off;

 # Misc

 client_max_body_size 16m;
 index index.html;

 # Proxy

 proxy_pass_request_body on;
 proxy_pass_request_headers on;
 proxy_redirect off;

 # Headers

 more_clear_headers Server;

 # Includes

 include sites-enabled/*;

 }

.. warning:: almost 1 minute to start the service

::

 ssl_stapling on;
 ssl_stapling_verify on;

Security
^^^^^^^^

* /etc/nginx/https.conf

::

 listen 443 ssl http2;
 listen [::]:443 ssl http2;

 error_page 496 =496 @error; # Certificate Required
 error_page 497 =497 @error; # HTTP Request Sent to HTTPS Port
 error_page
 403 # Forbidden
 404 # Not Found
 @error;

 add_header Expect-CT "enforce,max-age=0" always;
 add_header Referrer-Policy "no-referrer-when-downgrade" always;
 add_header Strict-Transport-Security "max-age=31557600;includeSubDomains;preload" always;
 add_header X-Content-Type-Options "nosniff" always;
 add_header X-Frame-Options "DENY" always;
 set $fp "";
 set $fp "${fp}accelerometer 'none';";
 set $fp "${fp}ambient-light-sensor 'none';";
 set $fp "${fp}animations 'self';";
 set $fp "${fp}autoplay 'none';";
 set $fp "${fp}camera 'none';";
 set $fp "${fp}document-domain 'none';";
 set $fp "${fp}document-write 'none';";
 set $fp "${fp}encrypted-media 'none';";
 set $fp "${fp}fullscreen *;";
 set $fp "${fp}geolocation 'none';";
 set $fp "${fp}gyroscope 'none';";
 set $fp "${fp}legacy-image-formats 'none';";
 set $fp "${fp}magnetometer 'none';";
 set $fp "${fp}microphone 'none';";
 set $fp "${fp}midi 'none';";
 set $fp "${fp}payment 'self';";
 set $fp "${fp}picture-in-picture 'none';";
 set $fp "${fp}speaker 'self';";
 set $fp "${fp}sync-xhr 'none';";
 set $fp "${fp}unsized-media 'none';";
 set $fp "${fp}usb 'none';";
 set $fp "${fp}vertical-scroll 'self';";
 set $fp "${fp}vr 'none';";
 add_header Feature-Policy "${fp}" always;

.. todo:: find policy not blocking sphinx search

::

 add_header Content-Security-Policy "default-src 'self'" always;

* /etc/nginx/uwsgi.conf

::

 uwsgi_param client_address   ${remote_addr};
 uwsgi_param client_port      ${remote_port};
 uwsgi_param client_ciphers   ${ssl_ciphers};
 uwsgi_param client_curves    ${ssl_curves};

 uwsgi_param session_reused   ${ssl_session_reused};
 uwsgi_param session_id       ${ssl_session_id};
 uwsgi_param session_cipher   ${ssl_cipher};
 uwsgi_param session_protocol ${ssl_protocol};

 uwsgi_param server_protocol  ${server_protocol};
 uwsgi_param server_address   ${server_addr};
 uwsgi_param server_port      ${server_port};

 uwsgi_param request_scheme   ${scheme};
 uwsgi_param request_host     ${host};
 uwsgi_param request_document ${document_uri};
 uwsgi_param request_query    ${query_string};
 uwsgi_param request_method   ${request_method};

 uwsgi_param content_type     ${content_type};
 uwsgi_param content_length   ${content_length};

 uwsgi_param client_verify    ${ssl_client_verify};
 uwsgi_param client_issuer    ${ssl_client_i_dn};
 uwsgi_param client_subject   ${ssl_client_s_dn};
 uwsgi_param client_start     ${ssl_client_v_start};
 uwsgi_param client_remain    ${ssl_client_v_remain};
 uwsgi_param client_end       ${ssl_client_v_end};

Apps
^^^^

* /etc/uwsgi/apps-enabled/root.ini

.. code:: ini

 [uwsgi]
 chown-socket = user
 uid = user
 gid = user
 chdir = /d/projects/rwx.work/root
 plugins = python3
 module = __init__
 callable = app
 threads = 2

Sites
^^^^^

* "/etc/nginx/sites-enabled/0 http"

::

 server {
 listen 80 default_server;
 listen [::]:80 default_server;
 server_name _;
 return 301 https://${host}${request_uri};
 }

* "/etc/nginx/sites-enabled/1 rwx.work"

::

 server {
 include rwx.work.conf;
 include uwsgi.conf;
 server_name .rwx.work;
 location / {
 uwsgi_pass unix:/run/uwsgi/app/root/socket;
 }
 }

 server {
 include rwx.work.conf;
 server_name deb.rwx.work;
 root /d/mirrors/apt-mirror/debian;
 fancyindex on;
 }

 server {
 include rwx.work.conf;
 server_name git.rwx.work;
 root /d/projects/rwx.work;
 fancyindex on;
 }

 server {
 include rwx.work.conf;
 server_name docs.rwx.work;
 root /d/projects/rwx.work/docs/out/docs;
 }

 server {
 include rwx.work.conf;
 server_name sites.rwx.work;
 root /d/projects/rwx.work/sites/out/sites;
 }

 server {
 include rwx.work.conf;
 server_name todo.rwx.work;
 root /d/projects/rwx.work/todo/out/todo;
 }

* "/etc/nginx/sites-enabled/2 marc-beninca.fr"

::

 server {
 include marc-beninca.fr.conf;
 include uwsgi.conf;
 server_name .marc-beninca.fr;
 location / {
 uwsgi_pass unix:/run/uwsgi/app/root/socket;
 }
 }

 server {
 include marc-beninca.fr.conf;
 server_name docs.marc-beninca.fr;
 root /d/projects/marc-beninca.fr/docs/out/docs;
 }

 server {
 include marc-beninca.fr.conf;
 server_name sites.marc-beninca.fr;
 root /d/projects/marc-beninca.fr/sites/out/sites;
 }

 server {
 include marc-beninca.fr.conf;
 server_name todo.marc-beninca.fr;
 root /d/projects/marc-beninca.fr/todo/out/todo;
 }

* "/etc/nginx/sites-enabled/3 tilde.link"

::

 server {
 include tilde.link.conf;
 include uwsgi.conf;
 server_name .tilde.link;
 location / {
 uwsgi_pass unix:/run/uwsgi/app/root/socket;
 }
 }

 server {
 include tilde.link.conf;
 server_name docs.tilde.link;
 root /d/projects/tilde.link/docs/out/docs;
 }

Certificate and errors
^^^^^^^^^^^^^^^^^^^^^^

* /etc/nginx/rwx.work.conf

::

 include https.conf;
 ssl_certificate rwx.work.crt;
 ssl_certificate_key rwx.work.key;
 location @error {
 return https://rwx.work/error/${status};
 }

* /etc/nginx/marc-beninca.fr.conf

::

 include https.conf;
 ssl_certificate marc-beninca.fr.crt;
 ssl_certificate_key marc-beninca.fr.key;
 location @error {
 return https://marc-beninca.fr/error/${status};
 }

* /etc/nginx/tilde.link.conf

::

 include https.conf;
 ssl_certificate tilde.link.crt;
 ssl_certificate_key tilde.link.key;
 location @error {
 return https://tilde.link/error/${status};
 }

* /etc/nginx/rwx.work.key
* /etc/nginx/rwx.work.crt

* /etc/nginx/marc-beninca.fr.key
* /etc/nginx/marc-beninca.fr.crt

* /etc/nginx/tilde.link.key
* /etc/nginx/tilde.link.crt
