Unbound
=======

* /etc/unbound/unbound.conf

  ::

   include: "/etc/unbound/unbound.conf.d/*.conf"

* /etc/unbound/unbound.conf.d/*.conf

  ::

   server:
   access-control: 192.168.0.0/16 allow
   do-ip4: yes
   do-ip6: yes
   do-tcp: yes
   do-udp: yes
   rrset-roundrobin: yes

   forward-zone:
   name: "."
   forward-addr: 9.9.9.9

   local-zone: "sub.domain.tld" static
   local-data: "sub.domain.tld 3600 IN A 1.2.3.4"
   local-data: "sub.domain.tld 3600 IN A 5.6.7.8"
   local-data-ptr: "1.2.3.4 sub.domain.tld"
   local-data-ptr: "5.6.7.8 sub.domain.tld"

   local-zone: "doubleclick.net" redirect
   local-data: "doubleclick.net A 127.0.0.1"
