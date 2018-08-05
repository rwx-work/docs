Services
========

user
----

.. code:: shell

 systemctl --user enable name.service
 loginctl enable-linger
 systemctl --user start name.service

.. info::

 enable-linger prevents daemon to be killed at session exit
