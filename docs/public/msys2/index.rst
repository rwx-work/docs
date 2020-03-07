msys2
=====

.. todo:: description

Configure
---------

* unarchive msys2-base-x86_64-YYYYMMDD.tar.xz

* edit /etc/pacman.conf

.. code:: ini

 [options]
 ILoveCandy

.. todo:: disable mingw32 group

* edit /etc/pacman.d/mirrorlist.msys

.. code:: ini

 Server = http://
 Server = file:///c/

.. todo:: mingw64 mirrorlist

* run msys2_shell.cmd
* close window at the end of the process

user
^^^^

* edit ~/.profile

.. code:: shell

 source /usr/share/git/git-prompt.sh

.. todo:: test if exists

Use
---

* run msys2_shell.cmd

.. todo:: optional mingw64 argument

.. code:: shell

 pacman -Syu

.. code:: shell

 pacman -S package1 …

.. code:: shell

 pacman -Scc

Packages
--------

mingw
^^^^^

* mingw-w64-x86_64-putty

msys
^^^^

* upx

broken
^^^^^^

* mingw-w64-x86_64-darktable
* mingw-w64-x86_64-inkscape

test
^^^^

* bc
* binutils
* dos2unix
* emacs
* fish
* git
* make
* man
* markdown
* mc
* nano
* openssh
* p7zip
* pass
* pwgen
* python
* rsync
* subversion
* tar
* tig
* tmux
* tree
* vim
* xorriso
* zsh
