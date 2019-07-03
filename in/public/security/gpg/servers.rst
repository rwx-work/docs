Servers
=======

Search
------

.. code:: shell

 gpg --search-keys "Key ID" \
 --keyserver hkps://sub.domain.tld

Download
--------

.. code:: shell

 gpg --receive-keys "Key ID" \
 --keyserver hkps://sub.domain.tld

Upload
------

.. code:: shell

 gpg --send-keys "Key ID" \
 --keyserver hkps://sub.domain.tld

Available
---------

Mitigated
^^^^^^^^^

* hkps://

::

 keys.openpgp.org

Vulnerable
^^^^^^^^^^

* hkps://

::

 keyring.debian.org
 pgp.key-server.io
 pgp.mit.edu
 peegeepee.com
 pgp.rediris.es
 sks-keyservers.net
 pgp.surfnet.nl
 keyserver.ubuntu.com

 # round-robin
 keys.gnupg.net

* hkp://

::

 pgp.uni-mainz.de

* not sure

::

 keyserver.oeg.com.au
