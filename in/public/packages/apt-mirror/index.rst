apt-mirror
==========

.. todo:: list files syntax

.. warning::

 Translations archived in xz are not fetched

Workaround:

::

 if ( $filename =~ m{^$component/i18n/Translation-[^./]*\.bz2$} )

::

 if ( $filename =~ m{^$component/i18n/Translation-[^./]*\.(bz2|xz)$} )
