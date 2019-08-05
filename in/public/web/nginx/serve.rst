Serve
=====

* /etc/nginx/sites-available/…

::

    server {
        listen 80;
        server_name _;
        location "/mirrors" {
            root "/";
            autoindex on;
        }
        location "/" {
            root "/data/http";
            autoindex on;
        }
    }
    server {
        listen 443 ssl http2;
        server_name "sous.domaine.tld";
        ssl_certificate "/etc/nginx/certificates/nom.crt";
        ssl_certificate_key "/etc/nginx/certificates/nom.key";
        location "/static" {
            root "/data/https";
            default_type "text/html";
            index "index.html";
        }
        location "/" {
            proxy_pass "http://127.0.0.1:8069";
            proxy_redirect off;
            proxy_set_header Host $host;
        }
    }

Redirect http to https
----------------------

::

 server {
 listen 80 default_server;
 listen [::]:80 default_server;
 server_name _;
 return 301 https://${host}${request_uri};
 }
