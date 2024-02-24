# create a file in /tmp
file {'~/.ssh/school/config':
    ensure  => file,
    content => "
        Host *
            IdentityFile ~/.ssh/school
            PasswordAuthentication no
    "
}
