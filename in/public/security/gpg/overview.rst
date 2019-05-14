********
OverView
********

.. todo::

 * setpref, or elsehow at key generation
 * ! suffix to exclude subkeys
 * trust
 * sign
 * delete

Search
======

.. code:: shell

  gpg --search-keys "Key ID"

Download
========

.. code:: shell

  gpg --receive-keys "KEY ID"

List
====

.. code:: shell

  gpg --list-keys

.. code:: shell

  gpg --list-signatures

Modify
======

.. code:: shell

  gpg --expert --edit-key "KEY ID"

[…]

::

  save

add a subkey to a master key
----------------------------

::

  addkey
  8 → RSA (set your own capabilities)

[…]

::

  q → finished
  4096
  1y → key expires in 1 year
  y → this is correct
  y → really create

sign
^^^^

::

  e → toggle the encrypt capability

.. code:: shell

  gpg --quick-add-key FFIINNGGEERRPPRRIINNTT rsa4096 auth 1y
  gpg --quick-add-key FFIINNGGEERRPPRRIINNTT rsa4096 encr 1y
  gpg --quick-add-key FFIINNGGEERRPPRRIINNTT rsa4096 sign 1y

encrypt
^^^^^^^

::

  s → toggle the sign capability

authenticate
^^^^^^^^^^^^

::

  s → toggle the sign capability
  e → toggle the encrypt capability
  a → toggle the authenticate capability

set expiration date
-------------------

::

  expire
  1y
  y

add another UserID
------------------

::

  adduid
  First Last
  user@domain.tld
  comment
  o

set primary UserID
------------------

::

  uid 1
  primary

Export
======

private key
-----------

.. code:: shell

  gpg --armor --export-secret-keys FFIINNGGEERRPPRRIINNTT > key.gpg

private subkeys
---------------

.. code:: shell

  gpg --armor --export-secret-subkeys FFIINNGGEERRPPRRIINNTT > subkeys.gpg

public key
----------

.. code:: shell

  gpg --armor --export "Key ID" > id.asc

public SSH key
--------------

.. code:: shell

  gpg --armor --export-ssh-key "Key ID" > id.pub

Dump
====

.. code:: shell

  pgpdump pub.asc

Secure
======

hide the master key in an encrypted container
---------------------------------------------

* ~/.gnupg/private-keys-v1.d/KKEEYYGGRRIIPP.key

Upload
======

.. code:: shell

  gpg --send-keys "KEY ID"

Revoke
======

.. code:: shell

  gpg --import "FFIINNGGEERRPPRRIINNTT.rev"
  gpg --send-keys "KEY ID"
