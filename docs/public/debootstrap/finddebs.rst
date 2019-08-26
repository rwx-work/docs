find debs
=========

work out debs
-------------

* dists/${suite}/${component}/binary-${architecture}/Packages

..code:: bash

 required ← Priority: required
 base ← "apt apt-transport-https ca-certificates"

resolve deps
------------

* dists/${suite}/${component}/binary-${architecture}/Packages

..code:: bash

 packages ← Depends: …
