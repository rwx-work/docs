DNS
===

::

 $TTL 3600
 @ IN SOA dns200.anycast.me. tech.ovh.net. (
   2019082700   ; Serial
        86400   ; Refresh
         3600   ; Retry
      3600000   ; Expire
          300 ) ; Negative Cache TTL

 @ IN NS dns200.anycast.me.
 @ IN NS  ns200.anycast.me.

 ; mailbox.org

 c9e8c75cec08cbff50e7c33108bd12d30b862813.rwx.work. IN TXT a9a1e94fbc4aa297df829145c8c48e298fea5bb9

 rwx.work. IN MX 10 mxext1.mailbox.org.
 rwx.work. IN MX 10 mxext2.mailbox.org.
 rwx.work. IN MX 20 mxext3.mailbox.org.

 IN TXT "v=spf1 include:mailbox.org"

 ; acme-challenge

 _acme-challenge.rwx.work. 60 IN TXT 4JWiOzemeGXZ6TNTFUY9acNRBR9WgDyvT3hnfMmrUUE
 _acme-challenge.rwx.work. 60 IN TXT 7gPydde0lq6fp3j_I3APYi-xD4g7KzLueseQHjndveo

 rwx.work. CAA 128 issue "letsencrypt.org"
 rwx.work. CAA 128 issuewild "letsencrypt.org"

 ; domain.tld

 * IN CNAME rwx.work.

 @ IN A    192.99.14.98
 @ IN AAAA 2607:5300:60:3f62::1
