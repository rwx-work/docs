Certificate
===========

Request
-------

.. code:: shell

 echo -n "\
 FR
 Gironde
 Bordeaux
 Marc Beninca
 .
 rwx.work
 tls@rwx.work
 .
 .
 " \
 | \
 openssl \
 req \
 -new \
 -utf8 \
 -key "rwx.work.key" \
 -out "rwx.work.csr" \
 -addext "subjectAltName=DNS:*.rwx.work"

::

 ?

Certificate
-----------

::

 ?
