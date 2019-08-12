#######
OpenSSL
#######

List secure ciphers
===================

.. code:: shell

 openssl ciphers ALL \
 | sed "s/:/\n/g" \
 | grep "\(TLS\|ECDHE\)" \
 | grep "\(POLY1305\|GCM\)" \
 | grep --invert-match "\(DSA\|PSK\|128\)"

Select cipher suites
====================

* /etc/ssl/openssl.cnf

::

 [system_default_sect]
 CipherSuites="TLS_CHACHA20_POLY1305_SHA256:TLS_AES_256_GCM_SHA384:TLS_AES_128_GCM_SHA256"

List curves
===========

.. code:: shell

 openssl ecparam -list_curves

Generate DHparam file
=====================

.. code:: shell

 openssl dhparam -out dhparam 4096

Generate private key
====================

RSA
---

.. code:: shell

  openssl \
  genrsa \
  -out "private_key.pem" \
  4096

Human readable:

.. code:: shell

  openssl \
  rsa \
  -in "private_key.pem" \
  -text \
  -noout \
  > "private_key.txt"

ED25519
-------

.. code:: shell

  openssl \
  genpkey \
  -algorithm ED25519 \
  > "private_key.pem"

Human readable:

.. code:: shell

  openssl \
  pkey \
  -in "private_key.pem" \
  -text \
  -noout \
  > "private_key.txt"

Generate a certificate request
==============================

* generate a private key

* using . for empty fields, generate the request with:

  * Country Name (2 letter code)
  * State or Province Name (full name)
  * Locality Name (eg, city)
  * Organization Name (eg, company)
  * Organizational Unit Name (eg, section)
  * Common Name (e.g. server FQDN or YOUR name)
  * Email Address
  * A challenge password
  * An optional company name

.. code:: shell

  echo -n "\
  US
  Region / County (code)
  City / Place
  Group / Management / Unit
  Section
  certificate_name
  alias@domain.tld
  .
  .
  " \
  | \
  openssl \
  req \
  -new \
  -utf8 \
  -key "private_key.pem" \
  -out "certificate_request.csr" \
  -addext "tlsfeature=status_request" \
  -addext "subjectAltName=DNS:*.domain.tld,DNS:*.sub.domain.tld"

Human readable:

.. code:: shell

  openssl \
  req \
  -in "certificate_request.csr" \
  -text \
  -noout \
  > "certificate_request.txt"

Create a Certification Authority
================================

init
----

.. code:: shell

  rm --force --recursive "demoCA"
  mkdir --parents "demoCA/newcerts"
  echo -n "" > "demoCA/index.txt"
  echo "00" > "demoCA/serial"

request
-------

.. code:: shell

  echo -n "\
  US
  Region / County (code)
  City / Place
  Decreasing / Hierarchy
  Name
  Name
  alias@domain.tld
  .
  .
  " \
  | \
  openssl \
  req \
  -new \
  -key "name.pem" \
  -out "name.csr" \
  -utf8 \

signature
---------

.. code:: shell

  openssl \
  ca \
  -selfsign \
  -in "name.csr" \
  -keyfile "name.pem" \
  -notext \
  -out "name.crt" \
  -startdate 20160801000000Z \
  -enddate 20180801000000Z \
  -batch \
  -extensions "v3_ca" \

----

quick & dirty variant
---------------------

.. code:: shell

  openssl \
  ca \
  -selfsign \
  -keyfile "private_key.pem" \

Sign request
============

.. code:: shell

  openssl \
  req \
  -in "certificate_request.csr" \
  -key "private_key.pem" \
  -x509 \
  -set_serial 0 \
  -days 730 \
  -out "certificate.crt" \
