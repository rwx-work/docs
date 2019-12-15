alsa
====

* /var/lib/alsa/asound.state

Unmute microphone
-----------------

.. code:: shell

 amixer -c 1 set Mic 100% unmute

Save settings
-------------

.. code:: shell

 alsactl store
