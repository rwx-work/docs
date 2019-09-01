fcgiwrap
========

.. todo:: mandatory parameters

Configure socket
----------------

.. code:: ini

 [Unit]
 Description=fcgiwrap socket

 [Socket]
 SocketMode=0600
 SocketUser=www-data
 SocketGroup=www-data
 ListenStream=/run/fcgiwrap.socket

 [Install]
 WantedBy=sockets.target

Configure service
-----------------

.. code:: ini

 [Unit]
 Description=simple cgi server
 After=nss-user-lookup.target
 Requires=fcgiwrap.socket

 [Service]
 Environment=DAEMON_OPTS=-f
 EnvironmentFile=-/etc/default/fcgiwrap
 ExecStart=/usr/sbin/fcgiwrap ${DAEMON_OPTS}
 User=www-data
 Group=www-data

 [Install]
 Also=fcgiwrap.socket
