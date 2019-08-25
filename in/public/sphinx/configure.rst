Configure documentation
=======================

* conf.py

Sphinx
------

.. code:: python3

 author = 'Author'
 copyright = ''
 extensions = [
     'sphinx.ext.autodoc',
     'sphinx.ext.doctest',
     'sphinx.ext.todo',
     'sphinx.ext.imgmath',
     'sphinx.ext.ifconfig',
     'sphinx.ext.viewcode',
 ]
 keep_warnings = False
 language = 'en'
 master_doc = 'index'
 project = 'Project'
 pygments_style = 'sphinx'
 release = ''
 show_authors = False
 source_suffix = [
     '.rst',
 ]
 todo_include_todos = True
 version = ''

HTML
----

.. code:: python3

 html_show_copyright = False
 html_show_sourcelink = True
 html_show_sphinx = False
 html_theme = 'sphinx_rtd_theme'
 html_title = 'Title'
 html_use_smartypants = False

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
