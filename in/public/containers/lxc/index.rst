###
LXC
###

.. toctree::

   host
   container
   unprivileged

***
ESX
***

.. warning::

  | If the host is part of an ESX virtual network architecture,
  | make sure to configure its virtual switch to avoid packet drops.

* Edit Settings / Policies / Security

=================== ======
Key                 Value
=================== ======
Promiscuous Mode    Accept
MAC Address Changes Accept
Forged Transmits    Accept
=================== ======

.. todo:: same problem with VirtualBox network
