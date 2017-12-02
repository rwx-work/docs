********
Snippets
********

Start a runnable script file
============================

.. code:: bash

  #! /bin/bash

Find out current script
=======================

.. code:: bash

  SCRIPT_FILE="$(realpath "${BASH_SOURCE[0]}")"
  SCRIPT_DIRECTORY="$(dirname "${SCRIPT_FILE}")"
  SCRIPT_NAME="$(basename "${SCRIPT_FILE}")"

Quit the interpreter
====================

.. code:: bash

  exit
