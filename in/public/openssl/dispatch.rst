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
 CipherSuites="TLS_CHACHA20_POLY1305_SHA256:TLS_AES_256_GCM_SHA384"

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
  -addext "subjectAltName=DNS:*.domain.tld,DNS:*.sub.domain.tld"

.. warning:: must staple, problems with nginx and apache

.. code:: shell

 -addext "tlsfeature=status_request"

Human readable:

.. code:: shell

  openssl \
  req \
  -in "certificate_request.csr" \
  -text \
  -noout \
  > "certificate_request.txt"

Export client P12/PFX
=====================

* client private key
* client certificate

.. code:: shell

 openssl \
 pkcs12 \
 -export \
 -out client.pfx \
 -inkey client.key \
 -in client.crt
