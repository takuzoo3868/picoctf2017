[](
  This markdown file is writeup template.
)
## keyz 20pt

### Problem
> While webshells are nice, it'd be nice to be able to login directly. To do so, please add your own public key to ~/.ssh/authorized_keys, using the webshell. Make sure to copy it correctly! The key is in the ssh banner, displayed when you login remotely with ssh, to shell2017.picoctf.com

### Answer
Implement public key authentication. Create a public key and a private key on the client side (`ssh-keygen -t rsa`). 
Copy and paste `is_rsa.pub` in home dir on the web-shell side. Next, copy to `.ssh/authorized_keys`.

```bash
- There is no authorized_keys ...
@shell-web:~$ mv ~/id_rsa.pub ~/.ssh/authorized_keys
@shell-web:~$ chmod 600 ~/.ssh/authorized_keys
- There is an authorized_keys ...
@shell-web:~$ cat ~/id_rsa.pub >> ~/.ssh/authorized_keys
@shell-web:~$ rm ~/id_rsa.pub
```

Check the remote access.

```bash
$ ssh takuzoo3868@shell2017.picoctf.com
Congratulations on setting up SSH key authentication!
Here is your flag: who_needs_pwords_anyways
takuzoo3868@shell-web:~$
```

### Flag
who_needs_pwords_anyways
