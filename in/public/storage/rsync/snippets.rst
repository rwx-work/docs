Snippets
========

Simulate sync with deletion
---------------------------

.. code:: shell

  rsync \
  --archive \
  --no-whole-file \
  --progress \
  --verbose \
  --delete --dry-run
  "/local/directory/" \
  "user@host:/remote/directory/"
