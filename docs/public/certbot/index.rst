certbot
=======

DNS certificate
---------------

.. code:: shell

 mkdir tmp
 certbot \
 --config-dir tmp \
 --logs-dir tmp \
 --work-dir tmp \
 certonly \
 --agree-tos \
 --manual \
 --manual-public-ip-logging-ok \
 --no-eff-email \
 --preferred-challenges dns \
 --email acme@domain.tld \
 --domains domain.tld,*.domain.tld \
 --csr file.csr
