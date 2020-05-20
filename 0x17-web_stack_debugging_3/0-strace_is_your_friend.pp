#Fix name file in wp-settings.php
exec {'name_file_fixed':
  path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command => "sed -i 's/phpp/php/g' /var/www/hemlt/wp-settings.php && service apache2 reload"
}
