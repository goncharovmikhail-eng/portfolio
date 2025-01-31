function passwdc() {
    local decrypted_file="/home/$USER/passwd"
    gpg --quiet --batch --yes --decrypt --output $decrypted_file /home/$USER/passwd.gpg
    cat $decrypted_file | grep $1
    shred -u $decrypted_file
}

function passwdw() {
    local decrypted_file="/home/$USER/passwd"
    local encrypt_file="/home/$USER/passwd.gpg"
    sudo chattr -i $encrypt_file
    gpg --quiet --batch --yes --decrypt --output $decrypted_file $encrypt_file
    nano $decrypted_file
    gpg --symmetric --batch --yes --output $encrypt_file $decrypted_file
    shred -u $decrypted_file
    chmod 700 $encrypt_file
    sudo chattr +i $encrypt_file
}
