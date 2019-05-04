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

Configure
=========

If up:

.. code:: shell

  killall -9 gpg-agent
  killall -9 dirmngr

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

  keyid-format long
  keyserver-options include-revoked
  list-options show-uid-validity
  verify-options show-uid-validity
  with-fingerprint
  with-keygrip
  with-subkey-fingerprint

  export-options export-minimal
  no-comments
  no-emit-version

  default-preference-list SHA512 AES256 BZIP2

  cert-digest-algo SHA512
  cipher-algo AES256
  compress-algo BZIP2
  digest-algo SHA512

  personal-cipher-preferences AES256
  personal-digest-preferences SHA512
  personal-compress-preferences BZIP2

  s2k-cipher-algo AES256
  s2k-digest-algo SHA512
  s2k-mode 3
  s2k-count 65011712

avoid DL/UL issues, depending on DNS
------------------------------------

* dirmngr.conf

::

  standard-resolver

authenticate
------------

* gpg-agent.conf

::

  enable-ssh-support

* sshcontrol

KeyGrip to use if there are several

::

  KKEEYYGGRRIIPP

* export SSH_AUTH_SOCK=$(gpgconf --list-dirs agent-ssh-socket)

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
  1y → key expires in 1 year
  y → this is correct
  First Last
  user@domain.tld
  comment
  o → ok

.. code:: shell

  gpg --quick-generate-key 'First Last <user@domain.tld>' rsa4096 cert 1y

revocation certificate
----------------------

.. code:: shell

  gpg --generate-revocation "KeyID" > "FFIINNGGEERRPPRRIINNTT.rev"

::

  y

::

  0 → no reason specified
  1 → key has been compromised
  2 → key is superseded
  3 → key is no longer used

::

  description
  y

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
