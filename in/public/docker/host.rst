Host
====

Stats
-----

.. code:: shell

 docker info

Images
------

List
^^^^

.. code:: shell

 docker images

Import
^^^^^^

.. code:: shell

 docker import archive_name.tar repository_name:image_name

Remove
^^^^^^

.. code:: shell

 docker image rm image_name

Containers
----------

List
^^^^

.. code:: shell

 docker ps --all

Create
^^^^^^

.. code:: shell

 docker create \
 --name container_name \
 --publish host_port:container_port \
 repository_name:image_name \
 command argument_1 …

Start
^^^^^

.. code:: shell

 docker start container_name

Stop
^^^^

.. code:: shell

 docker stop container_name

Remove
^^^^^^

.. code:: shell

 docker rm container_name
