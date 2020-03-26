#install and configure an Nginx server using Puppet instead of Bash
exec{ 'install and configure the Nginx server':
  path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command => "sudo apt-get update && sudo apt-get -y install nginx && echo -e 'Holberton School' > /var/www/html/index.html && sed -i '43i location /redirect_me{\nrewrite ^/(.*)$ https://www.youtube.com/watch?v=EgBJmlPo8Xw permanent;\n}\n' /etc/nginx/sites-available/default && service nginx start"
}
