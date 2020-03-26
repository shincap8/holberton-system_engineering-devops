#install and configure an Nginx server using Puppet instead of Bash
exec{ 'install':
  command  => "apt-get update && apt-get -y install nginx && echo 'Holberton School' > /var/www/html/index.html && sed -i '43i location /redirect_me{\nrewrite ^/(.*)$ https://www.youtube.com/watch?v=EgBJmlPo8Xw permanent;\n}\n' /etc/nginx/sites-available/default && service nginx start",
  provider => 'shell'
}
