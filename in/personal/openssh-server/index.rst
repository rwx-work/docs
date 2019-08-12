openssh-server
==============

::

 LogLevel INFO
 StrictModes yes
 Subsystem sftp internal-sftp

 AllowTcpForwarding yes
 Ciphers chacha20-poly1305@openssh.com,aes256-gcm@openssh.com
 Compression no
 MaxStartups 10:30:50
 PermitTunnel no
 Port 22
 TCPKeepAlive yes
 ClientAliveInterval 30
 X11Forwarding no

 AuthorizedKeysFile .ssh/authorized_keys
 ChallengeResponseAuthentication no
 FingerprintHash sha256
 HostbasedAuthentication no
 IgnoreRhosts yes
 HostKey /etc/ssh/ssh_host_ed25519_key
 HostKeyAlgorithms ssh-ed25519
 KexAlgorithms curve25519-sha256@libssh.org
 LoginGraceTime 60
 MACs hmac-sha2-512-etm@openssh.com
 PasswordAuthentication no
 PermitEmptyPasswords no
 PermitRootLogin prohibit-password
 PubkeyAuthentication yes
 UseDNS no
 UsePAM yes

 DebianBanner no
 PrintLastLog yes
 PrintMotd yes
 Banner none
 VersionAddendum none
