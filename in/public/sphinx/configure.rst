Configure documentation
=======================

MarkDown
--------

.. code:: python3

 source_parsers = {
     '.md': 'recommonmark.parser.CommonMarkParser',
 }
 source_suffix = ['.rst', '.md']

LaTeX
-----

.. code:: python3

 latex_elements = {
     'fontenc': r'\usepackage{fontspec}',
     'fontpkg': r'''
 \setmainfont{DejaVu Serif}
 \setsansfont{DejaVu Sans}
 \setmonofont{DejaVu Sans Mono}
 ''',
     'papersize': 'a4paper',
     'pointsize': '12pt',
 }
 latex_documents = [
     (master_doc, 'FileName.tex', 'Title',
      'Author', 'howto/manual'),
 ]
 latex_use_parts = False
 latex_keep_old_macro_names = False
