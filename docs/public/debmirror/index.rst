debmirror
=========

traditional
-----------

.. code:: shell

 debmirror \
 --source \
 --method="http" \
 --host="sub.domain.tld" \
 --root="path/resource" \
 --dist="buster" \
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
 "mirrors_directory/name"

debian only
-----------

.. code:: shell

 --di-arch="arches" \
 --di-dist="buster" \
 --i18n \
 --keyring="/usr/share/keyrings/debian-archive-keyring.gpg" \

violations
----------

.. code:: shell

 --no-source \
 --method="https" \
 --root="/" \
 --ignore-missing-release \
 --dist="name,path/resource" \
 --section="other,1.2/main" \
