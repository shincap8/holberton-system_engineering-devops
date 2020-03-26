#install and configure an Nginx server using Puppet instead of Bash
exec { 'install and configure':
  command  => "apt-get update && apt-get -y install nginx && echo -e 'Holberton School' > /var/www/html/index.html && sed -i '/listen 80 default_server;/a rewrite ^/redirect_me https://www.youtube.com/watch?v=EgBJmlPo8Xw permanent;' /etc/nginx/sites-available/default && service nginx start",
  provider => 'shell',
}
