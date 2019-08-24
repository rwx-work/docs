Render
======

.. todo:: ffmpeg pipe

.. code:: bash

   gource \
   --date-format "%Y - %m - %d  /  %H : %M : %S" \
   -f \
   --highlight-dirs \
   --highlight-users \
   --key \
   --output-framerate 60 \
   --start-date "yyyy-mm-dd HH:MM:SS" \
   --auto-skip-seconds 1 \
   --seconds-per-day 10
