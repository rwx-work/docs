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
  no-verbose
  verify-options show-uid-validity
  with-fingerprint
  with-keygrip
  with-subkey-fingerprint

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

  keyserver hkps://keys.openpgp.org
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
