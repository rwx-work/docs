C
=

Main
----

.. code:: c

 #include <stdio.h>

 main() {
     printf("Hello, world!\n");
     system("pause");
 }

Input
-----

.. code:: c

 int entry1 = 0;
 char operator;
 int entry2 = 0;
 printf("type in 2 integers\n");
 scanf("%d%s%d", &entry1, &operator, &entry2);
 printf("sum: %d\n", entry1 + entry2);

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
