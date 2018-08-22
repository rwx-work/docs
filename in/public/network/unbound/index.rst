Unbound
=======

* /etc/unbound/unbound.conf

  ::

    server:
        access-control: 192.168.0.0/24 allow
        access-control: 192.168.1.0/24 allow
        do-ip4: yes
        do-ip6: yes
        do-tcp: yes
        do-udp: yes
        interface: 0.0.0.0
        interface: ::0
        rrset-roundrobin: yes

    include: "/etc/unbound/unbound.conf.d/*.conf"

    forward-zone:
        name: "."
        forward-addr: 9.1.2.3
        forward-addr: 9.4.5.6
        forward-addr: 9.7.8.9

* /etc/unbound/unbound.conf.d/redirect.conf

  ::

    server:
        local-zone: "doubleclick.net" redirect
        local-data: "doubleclick.net A 127.0.0.1"

* /etc/unbound/unbound.conf.d/static.conf

  ::

    server:
        local-zone: "sub.domain.tld" static
        local-data: "sub.domain.tld 3600 IN A 1.2.3.4"
        local-data: "sub.domain.tld 3600 IN A 5.6.7.8"
        local-data-ptr: "1.2.3.4 sub.domain.tld"
        local-data-ptr: "5.6.7.8 sub.domain.tld"
