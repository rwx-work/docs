Servers
=======

Search
------

.. code:: shell

 gpg \
 --keyserver hkps://sub.domain.tld \
 --search-keys "Key ID"

Download
--------

.. code:: shell

 gpg \
 --keyserver hkps://sub.domain.tld \
 --receive-keys "Key ID"

Upload
------

.. code:: shell

 gpg \
 --keyserver hkps://sub.domain.tld \
 --send-keys "Key ID"

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
