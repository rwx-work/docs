###############
ISC-DHCP-server
###############

*************
Configuration
*************

* /etc/dhcp/dhcpd.conf

::

  option domain-name "sub.domain.tld";
  option domain-name-servers 1.2.3.200;

  default-lease-time 600;
  max-lease-time 7200;

  authoritative;

  subnet 1.2.3.0 netmask 255.255.255.0 {
      range 1.2.3.123 1.2.3.128;
  }
  host name {
      hardware ethernet 01:23:45:67:89:ab;
      fixed-address 1.2.3.4;
  }
