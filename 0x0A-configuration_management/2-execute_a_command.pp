# The file executes a command
exec { 'kill a proc':
  command => 'pkill killmenow',
  path    => '/usr/bin'
}
