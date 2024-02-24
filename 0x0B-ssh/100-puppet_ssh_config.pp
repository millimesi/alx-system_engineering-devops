# create a file with puppet
include stdlib

file_line { 'Turn off passwd auth':
  path  => '/etc/ssh/ssh_config',  
  line  => 'PasswordAuthentication no',
  match => '^#?PasswordAuthentication',
}

file_line { 'Declare identity file':
  path  => '/etc/ssh/ssh_config',  
  line  => 'IdentityFile ~/.ssh/school',
  match => '^#?IdentityFile',
}

file_line { 'Set up SSH client for my_server':
  path  => '/etc/ssh/ssh_config',  
  line  => 'HostName 100.25.177.26',
  match => '^#?HostName',
}

file_line { 'Set up SSH client user for my_server':
  path  => '/etc/ssh/ssh_config',  
  line  => 'User ubuntu',
  match => '^#?User',
}