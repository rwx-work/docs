Snippets
========

Simulate sync with deletion
---------------------------

.. code:: shell

 rsync \
 --archive \
 --chown user:group \
 --no-whole-file \
 --progress \
 --verbose \
 "/local/directory/" \
 "user@host:/remote/directory/" \
 --delete --delete-before --delete-after \
 --dry-run
