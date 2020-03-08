windows
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

Virtualization registry keys
----------------------------

HKEY_LOCAL_MACHINE

* SYSTEM\\ControlSet001\\Services\\hvservice
* SYSTEM\\ControlSet001\\Control\\DeviceGuard
* SOFTWARE\\Policies\\Microsoft\\Windows\\DeviceGuard

.. todo:: find out critical ones
