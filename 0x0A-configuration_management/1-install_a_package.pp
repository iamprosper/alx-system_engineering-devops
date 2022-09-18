# This file install flask from pip3
exec {'install flask from pip3',
  command => 'pip3 install flask==2.1.0',
  path    => ['/usr/bin']
}
