smtp
====

Email with attachment
---------------------

::

 Content-Type: multipart/mixed; boundary="${separator}"; charset="utf8"
 From: first.last@sub.domain.tld
 To: first.last@sub.domain.tld
 Subject: Email subject
 --${separator}
 Content-Type: text/plain; charset="utf8"

 Email body
 --${separator}
 Content-Disposition: attachment; filename="file name"
 Content-Transfer-Encoding: base64
 Content-Type: application/octet-stream

 …
 --${separator}--
