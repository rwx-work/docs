******
Syntax
******

Sections
========

.. code:: restructuredtext

  ####
  Part
  ####

  *******
  Chapter
  *******

  Section
  =======

  SubSection
  ----------

  SubSubSection
  ^^^^^^^^^^^^^

  Paragraph
  """""""""

Links
=====

Internal
--------

declaration
^^^^^^^^^^^

.. code:: restructuredtext

 .. label_name:

reference
^^^^^^^^^

.. code:: restructuredtext

 :ref:`label_name`_

ToSort
======

.. code:: restructuredtext

  .. raw:: html

     <div></div>

* *1 star*
* **2 stars**
* ``2 backquotes``

| After this comma,
| output new line
|

.. image:: image.png

.. this is a really useless comment

..
    multiline

    comment

Indent 0

  Indent 1 which
  continues here.

    Indent 2

* item

  * subitem

* item

#. first
#. second

----

.. epigraph::

  No matter where you go, there you are.

  -- Buckaroo Banzai
