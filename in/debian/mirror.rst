******
Mirror
******

apt-mirror
==========

.. todo:: syntax

debmirror
=========

traditional
-----------

.. code:: shell

  debmirror \
  --source \
  --method="http" \
  --host="sous.domaine.tld" \
  --root="chemin/ressource" \
  --dist="stretch" \
  --section="main" \
  --keyring="/etc/apt/trusted.gpg" \
  --arch="amd64" \
  --check-gpg \
  --checksums \
  --diff="none" \
  --postcleanup \
  --progress \
  --rsync-extra="none" \
  --timeout=360000 \
  --verbose \
  "répertoire_miroirs/nom" \

debian only
-----------

.. code:: shell

  --di-arch="arches" \
  --di-dist="stretch" \
  --i18n \
  --keyring="/usr/share/keyrings/debian-archive-keyring.gpg" \

violations
----------

.. code:: shell

  --no-source \
  --method="https" \
  --root="/" \
  --ignore-missing-release \
  --dist="nom,chemin/ressource" \
  --section="autre,1.2/main" \
