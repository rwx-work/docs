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
