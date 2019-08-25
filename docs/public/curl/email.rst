Send email
==========

.. code:: shell

 curl \
 --verbose \
 --insecure \
 --ssl-reqd \
 --url "smtp://sub.domain.tld" \
 --mail-from "first.last@sub.domain.tld" \
 --mail-rcpt "first.last@sub.domain.tld" \
 --user "login:password" \
 --upload-file -
