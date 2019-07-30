“Choose” fingerprint
====================

.. code:: bash

 #! /bin/bash

 mkdir --parents _

 while true; do

 gpg \
 --batch \
 --passphrase '' \
 --quick-generate-key \
 'First Last <first-last@domain.tld>' \
 ed25519 \
 cert \
 1y \
 &> /dev/null

 gpg \
 --armor \
 --export-secret-keys \
 'First Last' > "tmp.gpg"

 name=$(\
 cat tmp.gpg \
 | gpg --list-packets \
 | grep v4 \
 | awk -F ' ' '{print $9}' \
 | awk -F ')' '{print $1}' \
 )

 name="${name:24:4}_${name:28:4}__${name:32:4}_${name:36}"
 echo "${name}"
 mv tmp.gpg "_/${name}"

 rm openpgp-revocs.d/*
 rm private-keys-v1.d/*

 gpg \
 --batch \
 --yes \
 --delete-keys 'First Last'

 rm pubring.kbx*
 rm trustdb.gpg

 done
