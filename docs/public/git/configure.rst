Configure
=========

Identity
--------

.. code:: shell

  git config user.name "First Last"
  git config user.email "user@domain.tld"

* ~/.gitconfig

.. code:: ini

  [user]
      name = "First Last"
      email = "user@domain.tld"

Auto-build
----------

.. code:: shell

 git config receive.denyCurrentBranch updateInstead

* .git/hooks/post-receive (+x)

.. code:: shell

 #! /bin/sh
 ../build_script
