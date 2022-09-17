# using Puppet to make changes to our configuration file

exec { 'echo':
  path    => '/usr/bin:/bin:/usr/sbin',
  command => 'echo "    PasswordAuthentication no\n    IdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config',
}