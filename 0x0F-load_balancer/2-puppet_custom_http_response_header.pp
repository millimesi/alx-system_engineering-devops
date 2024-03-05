# Puppet script to install and configure Nginx server

# Update packages
exec { 'update':
  command => '/usr/bin/apt-get update',
}

# Install Nginx
-> package { 'nginx':
  ensure => 'present',
}

# Add custom HTTP header to Nginx configuration
-> file_line { 'http_header':
  path  => '/etc/nginx/nginx.conf',
  match => 'http {',
  line  => "http {\n\tadd_header X-Served-By \"${hostname}\";",
}

# Restart Nginx service
-> exec { 'run':
  command => '/usr/sbin/service nginx restart',
}
