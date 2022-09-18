# This file contain puppet script for ssh conf
exec { 'Change ssh configuration':
  command => 'echo "IdentityFile ~/.ssh/school\nPasswordAuthentication no" >> /etc/ssh/ssh_config',
  path    => '/usr/bin'
}
