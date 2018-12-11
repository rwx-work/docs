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

 void main() {
     system("pause");
 }

Declarations
------------

.. code:: c

 // unsigned, sizeof()
 char c = '1';
 short s = 2;
 int i = 4;
 long l = 8;
 float f = (float)4;
 double d = (double)8;
 long double ld = (long double)16;

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

.. code:: c

 do {
     expression1;
 } while (condition);
