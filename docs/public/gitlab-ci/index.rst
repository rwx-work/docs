gitlab-ci
=========

* /.gitlab-ci.yml

.. code:: yaml

 stages:
 - test
 - deploy

 try:
   stage: test
   image: alpine:latest
   script:
   - ls -al ../../..
   - ls -al ../..
   - ls -al ..
   - ls -al

 pages:
   stage: deploy
   script:
   - ls --all -l public
   artifacts:
     paths:
     - public

* group script

.. todo:: explain group logic

.. code:: shell

 apt update
 rm --force --recursive ../${group_project}
 apt --yes install git
 git clone ${group_url}/${group_project} ../${group_project}
 apt --yes install python3
 python3 ../${group_project}/buildeploy.py
