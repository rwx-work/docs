imagemagick
===========

configure
---------

* /etc/ImageMagick-6/policy.xml

.. code:: xml

 <policymap>
   <policy domain="resource" name="memory" value="1024MiB" />
 </policymap>

convert
-------

.. code:: shell

 convert \
 -units PixelsPerInch -density 300 \
 "${input_file}" "${output_file}"
