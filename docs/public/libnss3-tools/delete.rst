Delete
======

.. warning::

 deletion of key removes associated certificate

Key
---

.. code:: shell

 certutil \
 -d ~/.mozilla/firefox/default \
 -F -n "Name"

Certificate
-----------

.. code:: shell

 certutil \
 -d ~/.mozilla/firefox/default \
 -D -n "Name"
