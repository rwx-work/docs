***********************
Configure documentation
***********************

MarkDown
========

.. code:: python3

  source_parsers = {
      '.md': 'recommonmark.parser.CommonMarkParser',
  }
  source_suffix = ['.rst', '.md']
