#!/usr/bin/env bash
# sets up your web servers for the deployment

apt-get -y update
apt-get -y install nginx

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

echo "Holberton School" > /data/web_static/releases/test/index.html
ln -sL /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu /data/
chgrp -R ubuntu /data/

printf %s "server {
    listen 80 default_server;
    add_header X-Served-By $HOSTNAME;
    root  /var/www/html;
    index index.html index.ht


    location /hbnb_static/ {
        alias /data/web_static/current/;
        index index.html index.ht;
    }

    location /redirect_me {
        return 301 http://cuberule.com/;
    }
}" > etc/nginx/sites-available/default

service Nginx restart
