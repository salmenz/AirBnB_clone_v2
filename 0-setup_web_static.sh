#!/usr/bin/env bash
# Installs nginx, creates folders for deployment, updates Nginx configuration
apt-get -y update
apt-get -y install nginx
mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared
echo -e "
<html>
    <head></head>
    <body>
        Holberton School
    </body>
</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i '46 i\ \tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tindex index.html;\n\t}\n' /etc/nginx/sites-enabled/default
service nginx restart
