openssh-server
==============

::

 LogLevel INFO
 StrictModes yes
 Subsystem sftp internal-sftp
 UsePrivilegeSeparation sandbox

 AllowTcpForwarding yes
 Ciphers aes256-gcm@openssh.com
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
 HostKey /etc/ssh/ssh_host_ecdsa_key
 HostKeyAlgorithms ecdsa-sha2-nistp521-cert-v01@openssh.com,ecdsa-sha2-nistp521
 KexAlgorithms diffie-hellman-group18-sha512,diffie-hellman-group16-sha512
 LoginGraceTime 60
 MACs hmac-sha2-512-etm@openssh.com
 PasswordAuthentication no
 PermitEmptyPasswords no
 PermitRootLogin no
 PubkeyAuthentication yes
 UseDNS no
 UsePAM yes

 DebianBanner no
 PrintLastLog yes
 PrintMotd yes
 Banner none
 VersionAddendum none
