*****
Build
*****

Formats
=======

Documents
---------

* html5
* odt
* docx
* latex (--latex-engine="xelatex")

Presentations
-------------

* beamer
* dzslides
* revealjs
* s5
* slideous
* slidy

Generation
==========

.. code:: shell

  pandoc \
  --data-dir="directory/path" \
  --from="markdown" \
  "input_file" \
  --to="html5" \
  --output="output_file" \
  --standalone \
  --number-sections \
  --toc \
  --toc-depth=3 \
  --template="template_name" \
  --css="style/relative/path"
