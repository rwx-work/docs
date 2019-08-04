*********
Configure
*********

* /etc/nginx/nginx.conf

.. code::

 pid /run/nginx.pid;
 user user;
 worker_processes auto;

 events {
 multi_accept off;
 worker_connections 512;
 }

 http {

 # General

 keepalive_timeout 60;
 sendfile on;
 server_tokens off;
 tcp_nopush on;
 tcp_nodelay on;
 types_hash_max_size 2048;

 # Names

 server_name_in_redirect off;
 server_names_hash_bucket_size 128;

 # File types

 include /etc/nginx/mime.types;
 default_type application/octet-stream;

 # Security

 ssl_buffer_size 8k;
 ssl_ciphers "TLS_AES_256_GCM_SHA384,TLS_CHACHA20_POLY1305_SHA256,TLS_AES_128_GCM_SHA256,ECDHE-RSA-AES256-GCM-SHA384,ECDHE-RSA-CHACHA20-POLY1305,ECDHE-ARIA256-GCM-SHA384,ECDHE-RSA-AES128-GCM-SHA256,ECDHE-ARIA128-GCM-SHA256";
 ssl_ecdh_curve secp384r1;
 ssl_prefer_server_ciphers on;
 ssl_protocols TLSv1.3 TLSv1.2;
 ssl_session_cache shared:ssl_session_cache:16m;
 ssl_session_timeout 15m;

 # Log

 access_log /var/log/nginx/access.log;
 error_log /var/log/nginx/error.log;

 # Compression

 gzip off;

 # Misc

 add_header Strict-Transport-Security max-age=31557600;
 client_max_body_size 16m;
 index index.html;
 proxy_pass_request_body on;
 proxy_pass_request_headers on;
 proxy_redirect off;

 # Includes

 include /etc/nginx/sites-enabled/*;

 }
