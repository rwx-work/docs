Build documentation
===================

HTML
----

.. code:: python3

 import sphinx

 sphinx.build_main([
     '-E',
     '-j', '2',
     '-b', 'html',
     '-D', 'project=Project',
     '-c', conf_directory,
     input_directory,
     output_directory,
 ])

LaTeX
-----

.. code:: python3

 '-b', 'latex',

.. todo:: turn make command into xelatex command

.. code:: shell

 make PDFLATEX=xelatex -C build/latex all-pdf
