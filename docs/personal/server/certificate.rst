Certificate
===========

Request
-------

.. code:: shell

 echo -n "\
 FR
 Gironde
 Bordeaux
 Marc Beninca
 .
 rwx.work
 tls@rwx.work
 .
 .
 " \
 | \
 openssl \
 req \
 -new \
 -utf8 \
 -key "rwx.work.key" \
 -out "rwx.work.csr" \
 -addext "subjectAltName=DNS:*.rwx.work"

::

 -----BEGIN CERTIFICATE REQUEST-----
 MIIE5zCCAs8CAQAwejELMAkGA1UEBhMCRlIxEDAOBgNVBAgMB0dpcm9uZGUxETAP
 BgNVBAcMCEJvcmRlYXV4MRUwEwYDVQQKDAxNYXJjIEJlbmluY2ExETAPBgNVBAMM
 CHJ3eC53b3JrMRwwGgYJKoZIhvcNAQkBFg1tYXJjQHJ3eC53b3JrMIICIjANBgkq
 hkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAzFVnxoVca/cMv9HoOwOF6oYUiwXIuS8N
 QAWc9mqZowcIL0SEmC/kP+T2DMHR673Z9fCe2EXfG/Yfo/GRHB1zgUgjSKFWSCHA
 whk+72fnukX0XtJ+DXywMbPMSkSu6ppJlQvLxn59ya0bbhmZZnTGmK3GoVoyoMid
 sjLguNRRxSSuNiMbvN4alFxWztHhPfifS95DVAx2do8qaYFrIOIxZBne0KkzYKBo
 N/HH+HKaptYNgVtUvEYYQgW8zlUMd6i70HrVpNUMRlGpixB2jgEasgjrj4ICG/Gn
 rdw5mRtJ/a8lKx0l5YOzWik/6kSYK+2vffILxmn3NxCuE4UOgN+DK3Dke7+kHX53
 sLrwV5OMoqtln0ZJIprWWwlV58iTkNz12/tpcyV7NW3rQ448HqZTzXmsTu3t3hsK
 Y3HUuuGplLPp/P/fgNQMb4e58OTivs3JmA96MYcJ8hwmnpUQzbC5xjApHd5cD+mP
 3DEejwxLqQMpaielJ7dqWGywuxxbqHZ1rl5tHKDcD8sTfcryEM6IErlWGWEn6lZP
 lLREx7xa/g0cSVKSlnEpENDdwcs7cDgKEtRbZL+xxU9epNUsyxE0mm2YO8HFctGS
 lAlctOlxEXe/YdRJuonJ5tGqut9YzSCASF+OOmnyb0oYRLZz2/b8TsgD07TGALWO
 dsuHLBPvlD0CAwEAAaAoMCYGCSqGSIb3DQEJDjEZMBcwFQYDVR0RBA4wDIIKKi5y
 d3gud29yazANBgkqhkiG9w0BAQsFAAOCAgEAqkilUJUv66UEoNnvw1GHh8eTE9vc
 iae22pj+VScil1R8nesWiNP3FuDDYcMkBG2SAfiDnG4Ua9cmm3YeiTf0kkdAafnq
 oWM0YG7FM3b5TA9d+RUV2p5UIOZt1RLprcg/6TZv12lz5XCPYF+3YUqREzozTmZd
 lEnFtBns+QnsC6vMlEtEDqvUWhSYHFmJF4LoFH7u3A6Bsl5ge0bNrzl/LXj6/7Lt
 /4XQu1daWGvc5lrOhSzB+K7kiA5tYWjNCC4BFhufj8KBblzg4rNqRBTzU6BjzHfW
 R4X4C7fEmqQ0rDtdTYmhJRUwRV3dI2SpRnnXiQehAeUHj2ZUpvU0VmAymGXmM/2u
 o+dINwRbi5g4SNMDgiXu90zfYbhdH0YDFIClYCJyfedE0tYxLI+qLFjVnVRE0HO/
 vlFQluLN9UKd5AcWTCKMLqdDUi75oaSo2dZxQhDz3Dm1oxlormBK/vECjtTgmsKL
 VZeilFwLyvDaaM9zJf6d7mADrwD/LVuS4Hb6vhcdjMxqK1ULErBdhAnk8lyf9Po+
 iuo9FGfA/3I3iRZS8CntJbPQ+kIljJFkgoWR8tGZ2odrSjvjvdFS0UsRjRSa0FsV
 cj6qi6keDP8TdXGd4fs+o0bfjAbbRkvwksBYIW/1nVWm4pFCnHWArrPHbLmqlmig
 RD9FQO+ig4qr5yo=
 -----END CERTIFICATE REQUEST-----

Certificate
-----------

::

 ?
