wget
====

Mirror website
--------------

.. code:: shell

 wget \
 --mirror \
 --convert-links \
 --page-requisites \
 --continue \
 --no-parent \
 protocol://sub.domain.tld
