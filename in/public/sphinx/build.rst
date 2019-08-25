Build documentation
===================

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
