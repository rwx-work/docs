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
