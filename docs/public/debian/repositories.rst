************
Repositories
************

Keys
====

archive
-------

Master key

* E0B11894F66AEC98 Debian Archive Automatic Signing Key <ftpmaster@debian.org>

Subkey

* 04EE7237B7D453EC Debian Archive Automatic Signing Key (9/stretch) <ftpmaster@debian.org>

Deprecated

* 7638D0442B90D010 Debian Archive Automatic Signing Key (8/jessie) <ftpmaster@debian.org>

security
--------

* 9D6D8F6BC857C906 Debian Security Archive Automatic Signing Key (8/jessie) <ftpmaster@debian.org>

And, for some reason, this one used with testing/updates

* 8B48AD6246925553 Debian Archive Automatic Signing Key (7.0/wheezy) <ftpmaster@debian.org>

Locations
=========

* content delivery network

  * https://deb.debian.org/debian
  * https://deb.debian.org/debian-security

* legacy

  * http://ftp.fr.debian.org/debian
  * http://ftp.us.debian.org/debian
  * http://security.debian.org

Structure
=========

* ? changelogs
* ? DEP-11
* ? doc
* ? extrafiles
* ? indices

* dists

  * ?

* dists

  * oldstable
  * oldstable-backports
  * oldstable-updates
  * stable
  * stable-backports
  * stable-updates

Files
=====

README
------

============================= ===================================================
oldoldstable, or wheezy       the released Debian 7.11
oldstable, or jessie          the released Debian 8.9
stable, or stretch            the released Debian 9.2
oldoldstable-proposed-updates possible updates to Debian 7
oldstable-proposed-updates    possible updates to Debian 8
stable-proposed-updates       possible updates to Debian 9
wheezy-updates                important updates to Debian 7
jessie-updates                important updates to Debian 8
stretch-updates               important updates to Debian 9
testing, or buster            the development version of the next release
unstable, or sid              untested candidate packages for future releases
experimental, or rc-buggy     experimental packages to be used on top of unstable
============================= ===================================================

Release
-------

contrib main non-free

* ?/Contents-*
* ?/Contents-source
* ?/Contents-udeb-*
* ?/binary-all
* ?/binary-*
* ?/debian-installer/binary-all
* ?/debian-installer/binary-*
* ?/dep11/Components-*
* ?/dep11/icons
* ?/i18n
* main/installer-*
* ?/contrib/source

::

  Origin: Debian
  Label: Debian
  Suite: stable
  Version: 9.2
  Codename: stretch
  Changelogs: http://metadata.ftp-master.debian.org/changelogs/@CHANGEPATH@_changelog
  Date: Sat, 07 Oct 2017 09:44:42 UTC
  Acquire-By-Hash: yes
  Architectures: amd64 arm64 armel armhf i386 mips mips64el mipsel ppc64el s390x
  Components: main contrib non-free
  Description: Debian 9.2 Released 07 October 2017
  MD5Sum:
   f9bbab6d94f45e56c672017d8720a24c  1181459 contrib/Contents-amd64
   …
  SHA256:
   e3bf2ecc2ce89bc48e2339b86ceaba9e1fff7d6668eafab1445e7f7990c4802e  1181459 contrib/Contents-amd64
   …

Packages
--------

::

  Package: astrometry-data-2mass-00
  Source: astrometry-data-2mass
  Version: 1.1
  Installed-Size: 13882041
  Maintainer: Debian Astronomy Team <debian-astro-maintainers@lists.alioth.debian.org>
  Architecture: all
  Depends: astrometry.net, curl
  Enhances: astrometry.net
  Description: Astrometry.net 2MASS index files downloader (2'-2.8')
  Homepage: http://data.astrometry.net/4200
  Description-md5: b0effd246d35f7c4108f5a91527965cd
  Section: contrib/science
  Priority: optional
  Filename: pool/contrib/a/astrometry-data-2mass/astrometry-data-2mass-00_1.1_all.deb
  Size: 3204
  MD5sum: 1a51ad538ca17d1113802820856dc4d5
  SHA256: 36eafa5e9dbea55ecea5b2595f0d7c0a591e0831e20ac3ac98a239605074798a
