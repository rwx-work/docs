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

----

dirtier certificate only variant
--------------------------------

.. code:: shell

 openssl \
 req \
 -new \
 -x509 \
 -days 365 \
 -key ca.key \
 -out ca.crt

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

----

from CA key & certificate
-------------------------

.. code:: shell

 openssl \
 x509 \
 -CA ca.crt \
 -CAkey ca.key \
 -req \
 -in "client.csr" \
 -days 365 \
 -out "client.crt" \
 -set_serial nn
