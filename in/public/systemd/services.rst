Services
========

user
----

.. code:: shell

 systemctl --user enable name.service
 loginctl enable-linger
 systemctl --user start name.service

.. note::

 enable-linger prevents daemon to be killed at session exit

Example:

* ~/.config/systemd/user/multi-user.target.wants/httpy.service

.. code:: ini

 [Unit]
 Description=httpy
 After=network-online.target
 Wants=network-online.target

 [Service]
 ExecStart=/usr/bin/python3 -m http.server 8080
 WorkingDirectory=%h/www
 Restart=always

 [Install]
 WantedBy=multi-user.target

.. note::

 %h is replaced by the user's home directory
