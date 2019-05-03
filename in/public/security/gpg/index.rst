###
GPG
###

TODO
====

* setpref, or elsehow at key generation
* ! suffix to exclude subkeys
* trust
* sign
* delete
* ssh authentication ???

Configure
=========

If up:

.. code:: shell

  killall gpg-agent
  killall dirmngr

wipe if needed
--------------

.. code:: shell

  rm --force --recursive ~/.gnupg
  mkdir -m 700 ~/.gnupg

check available algorithms
--------------------------

.. code:: shell

  gpg --version

avoid default use of SHA256
---------------------------

* gpg.conf

::

  cert-digest-algo SHA512
  personal-digest-preferences SHA512
  personal-cipher-preferences CAMELLIA256 TWOFISH AES256
  personal-compress-preferences BZIP2 ZLIB ZIP
  default-preference-list SHA512 CAMELLIA256 TWOFISH AES256 BZIP2 ZLIB ZIP

  keyserver-options include-revoked


  with-keygrip
  with-subkey-fingerprint

avoid DL/UL issues, depending on DNS
------------------------------------

* dirmngr.conf

::

  standard-resolver

Generate
========

master key
----------

.. code:: shell

  gpg --expert --full-generate-key

::

  8 → RSA (set your own capabilities)
  s → toggle the sign capability
  e → toggle the encrypt capability
  q → finished
  4096
  2y → key expires in 2 years
  y → this is correct
  First Last
  user@domain.tld
  comment
  o → ok

.. code:: shell

  gpg --quick-generate-key 'First Last <user@domain.tld>' rsa4096 cert 2y

revocation certificate
----------------------

.. code:: shell

  gpg --generate-revocation "KeyID" > "FFIINNGGEERRPPRRIINNTT.rev"

.. warning::

  Hide this file in an encrypted container!

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
  PassPhrase

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

add another UserID
------------------

::

  adduid
  First Last
  user@domain.tld
  Comment

set primary UserID
------------------

::

  uid 1
  primary

Export
======

.. code:: shell

  gpg --armor --export "Key ID" > pub.asc

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
