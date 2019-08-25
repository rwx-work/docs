Sign certificate request
========================

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

from proper CA
--------------

.. code:: shell

  openssl \
  req \
  -in "certificate_request.csr" \
  -key "private_key.pem" \
  -x509 \
  -set_serial 0 \
  -days 730 \
  -out "certificate.crt"
