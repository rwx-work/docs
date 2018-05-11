##############
OpenSSH server
##############

*********
Configure
*********

* /etc/ssh/moduli

Generate usable prime numbers pool.

.. warning::

  These are **VERY** long operations!

.. code:: shell

  ssh-keygen -b 4096 -G 4096.G
  ssh-keygen -f 4096.G -T moduli

* /etc/ssh/ssh_host_*_key

types: rsa/ed25519/…?

.. code:: shell

  ssh-keygen -b 4096 -f /etc/ssh/ssh_host_rsa_key

* /etc/ssh/sshd_config

::

  # daemon
  AllowTcpForwarding yes
  ClientAliveInterval 30
  Compression no
  HostKey /etc/ssh/ssh_host_rsa_key
  IgnoreRhosts yes
  LogLevel INFO
  MaxStartups 16:32:64
  PermitTunnel no
  Port 22
  Protocol 2
  Subsystem sftp internal-sftp
  TCPKeepAlive yes
  UseDNS no
  UseLogin no
  UsePAM yes
  X11Forwarding no

  # authentication
  AuthorizedKeysFile .ssh/authorized_keys
  ChallengeResponseAuthentication no
  Ciphers chacha20-poly1305@openssh.com,aes256-gcm@openssh.com,aes256-ctr
  HostbasedAuthentication no
  KexAlgorithms curve25519-sha256@libssh.org,diffie-hellman-group-exchange-sha256
  LoginGraceTime 60
  MACs hmac-sha2-512-etm@openssh.com,hmac-sha2-256
  PasswordAuthentication no
  PermitEmptyPasswords no
  PermitRootLogin without-password
  PubkeyAuthentication yes
  StrictModes yes
  UsePrivilegeSeparation sandbox

  # prompt
  Banner none
  DebianBanner no
  PrintLastLog yes
  PrintMotd no
  VersionAddendum none

* authorized_keys

.. todo:: about
