# create a file in /tmp
file {'~/.ssh/school':
    ensure  => file,
    content => "
        Host *
            IdentityFile ~/.ssh/school
            PasswordAuthentication no
    "
}
