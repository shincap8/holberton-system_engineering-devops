#manifest that kills a process named killmenow.
exec { 'killmenow':
  path    => ['/usr/bin', '/bin', '/usr/local/bin'],
  command => 'pkill -f killmenow'
}
