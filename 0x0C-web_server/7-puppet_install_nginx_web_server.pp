# Puppet script to install and configure Nginx server

# installs the package
package { 'nginx':
  ensure => 'present',
}

# installs Nginx
exec { 'install':
  command  => 'sudo apt-get update ; sudo apt-get -y install nginx',
  provider => shell,
}

# Creates a Hello World html page
exec { 'Hello_world':
  command  => 'echo "Hello World!" | sudo tee /var/www/html/index.html',
  provider => shell,
}

# Redirects in the Nginx default site
exec { 'configure_redirect':
  command  => <<-EOT
    sudo sed -i "s/listen 80 default_server;/listen 80 default_server;\\n\\tlocation \\/redirect_me {\\n\\t\\treturn 301 https:\\/\\/www.google.com\\/;\\n\\t}/" /etc/nginx/sites-available/default
  EOT
  provider => shell,
}

# Restart Nginx
exec { 'restart_nginx':
  command  => 'sudo service nginx restart',
  provider => shell,
}
