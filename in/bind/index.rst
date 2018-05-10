####
BIND
####

******
Domain
******

* /etc/bind/named.conf.local

::

  zone "sub.domain.tld" {
      type master;
      file "/etc/bind/db.sub.domain.tld";
  };

  zone "3.2.1.in-addr.arpa" {
      type master;
      file "/etc/bind/db.3.2.1";
  };

* /etc/bind/db.sub.domain.tld

::

  $TTL 604800
  @ IN SOA ns.sub.domain.tld. admin.sub.domain.tld. (
        2 ; Serial
   604800 ; Refresh
    86400 ; Retry
  2419200 ; Expire
   604800 ; Negative Cache TTL
  )
  @ IN NS ns.sub.domain.tld.
  *.sub.domain.tld. IN A 1.2.3.78
  ns        IN A 1.2.3.12
  server    IN A 1.2.3.12
  dl        IN A 1.2.3.34
  www       IN A 1.2.3.56
  *.www     IN CNAME www

* /etc/bind/db.3.2.1

::

  $TTL 604800
  3.2.1.in-addr.arpa. IN SOA ns.sub.domain.tld. admin.sub.domain.tld. (
        1 ; Serial
   604800 ; Refresh
    86400 ; Retry
  2419200 ; Expire
   604800 ; Negative Cache TTL
  )
  3.2.1.in-addr.arpa.     IN NS  ns.sub.domain.tld.
  12.3.2.1.in-addr.arpa.  IN PTR server.sub.domain.tld.
  34.3.2.1.in-addr.arpa.  IN PTR dl.sub.domain.tld.
  56.3.2.1.in-addr.arpa.  IN PTR sub.domain.tld.
