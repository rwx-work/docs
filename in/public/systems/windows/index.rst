Windows
=======

.. warning:: v7 does BSOD if system partition beginning moves

Prevent short session lock timeout
----------------------------------

.vbs file:

.. code::

 set shell = wscript.createobject("wscript.shell")
 do while true
     shell.sendkeys("{NUMLOCK}{NUMLOCK}")
     wscript.sleep(1000*59)
 loop
