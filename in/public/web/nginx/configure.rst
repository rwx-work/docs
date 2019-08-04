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
     ssl_ciphers "ECDHE-RSA-AES256-GCM-SHA384,ECDHE-ECDSA-AES256-GCM-SHA384,ECDHE-RSA-AES256-SHA384,ECDHE-ECDSA-AES256-SHA384,ECDHE-RSA-AES256-SHA,ECDHE-ECDSA-AES256-SHA,DHE-DSS-AES256-GCM-SHA384,DHE-RSA-AES256-GCM-SHA384,DHE-RSA-AES256-SHA256,DHE-DSS-AES256-SHA256,DHE-RSA-AES256-SHA,DHE-DSS-AES256-SHA";
     ssl_dhparam /etc/nginx/dhparam;
     ssl_ecdh_curve secp384r1;
     ssl_prefer_server_ciphers on;
     ssl_protocols TLSv1.2;
     ssl_session_cache shared:ssl_session_cache:16m;
     ssl_session_timeout 15m;

     # Log

     access_log /var/log/nginx/access.log;
     error_log /var/log/nginx/error.log;

     # Compression

     gzip on;
     gzip_buffers 32 8k;
     gzip_comp_level 5;
     gzip_http_version 1.1;
     gzip_proxied any;
     gzip_types *;
     gzip_vary off;

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
