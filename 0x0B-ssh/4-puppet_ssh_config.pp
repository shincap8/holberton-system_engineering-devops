#make changes to our configuration file with Puppet
file_line { 'Turn off passwd auth':
  path  => '/etc/ssh/ssh_config',
  line  => 'PasswordAuthentication no'
  match => '^#   PasswordAuthentication yes'
}

file_line { 'Declare identity file':
  path  => '/etc/ssh/ssh_config',
  line  => 'IdentityFile ~/.ssh/holberton'
  match => '^#   IdentityFile ~/.ssh/id_rsa'
}
