gitweb
======

Configure
---------

.. todo:: /etc/gitweb.conf alike

Expose
------

.. todo:: link to fcgi common configuration

NginX
^^^^^

::

 location /static/ {
 root /usr/share/gitweb;
 }
 location / {
 include fcgi.conf;
 fastcgi_param SCRIPT_FILENAME /usr/share/gitweb/gitweb.cgi;
 fastcgi_param GITWEB_CONFIG /etc/gitweb.conf;
 fastcgi_pass unix:/run/fcgiwrap.socket;
 }
