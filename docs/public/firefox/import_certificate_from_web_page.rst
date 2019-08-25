Import certificate from web page
================================

Set the web server's MIME types

CA certificate
--------------

::

 application/x-x509-ca-cert   crt der pem;

Client certificate
------------------

.. warning:: doesn't work, bug still open

::

 application/x-x509-user-cert p12 pfx;
