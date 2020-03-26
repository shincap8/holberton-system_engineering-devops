#install and configure an Nginx server using Puppet instead of Bash
#install and configure an Nginx server using Puppet instead of Bash
exec{ 'update':
  path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command => 'sudo apt-get update',
}
exec{ 'install':
  path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command => 'sudo apt-get -y install nginx',
}
exec{ 'Holberton':
  path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command => "echo -e 'Holberton School' > /var/www/html/index.html",
}
exec{ 'Redirect':
  path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command => "sed -i '43i location /redirect_me{\nrewrite ^/(.*)$ https://www.youtube.com/watch?v=EgBJmlPo8Xw permanent;\n}\n' /etc/nginx/sites-available/default",
}
exec{ 'Start':
  path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command => 'service nginx start',
}
