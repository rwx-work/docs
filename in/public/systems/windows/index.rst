Windows
=======

.. warning:: v7 does BSOD if system partition beginning moves

Prevent short session lock timeout
----------------------------------

.vbs file:

.. code::

 Set shell = WScript.CreateObject("WScript.Shell")
 Do While True
     shell.sendkeys("{F15}")
     Wscript.Sleep(1000*59)
 Loop
