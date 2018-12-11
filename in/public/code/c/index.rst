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
 int entry2 = 0;
 printf("type in 2 integers\n");
 scanf("%d%d", &entry1, &entry2);
 printf("sum: %d\n", entry1 + entry2);
