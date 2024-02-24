# create a file in /tmp
file {'~/.ssh/config':
    ensure  => file,
    content => "
        Host *
            IdentityFile ~/.ssh/school
            PasswordAuthentication no
    "
}
