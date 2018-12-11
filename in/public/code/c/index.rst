C
=

Imports
-------

.. code:: c

 #include <stdio.h>

Comments
--------

.. code:: c

 // single line comment
 /* multi line comment */

Main
----

.. code:: c

 main() {
     system("pause");
 }

Declarations
------------

.. code:: c

 char operator;
 int entry1 = 0;
 int entry2 = 0;
 long entry = 0;
 float f = (float)1;

Output
------

.. code:: c

 printf("int: %d\n", entry1);
 printf("float: %.2f\n", f);

Input
-----

.. code:: c

 scanf("%d%s%d", &entry1, &operator, &entry2);

Conditions
----------

.. code:: c

 if (condition) {
     expression1;
 } else {
     expression2;
 }

.. code:: c

 switch (operator) {
     case '+':
         expression1;
         break;
     default:
         printf("Nope!\n");
 }

Loops
-----

.. code:: c

 for (declarations;conditions;increments) {
     expression1;
 }

.. code:: c

 while (condition) {
     expression1;
 }
