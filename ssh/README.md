# SSH

## Tasks 0–2

- `0-use_a_private_key <server-ip>` connects as `ubuntu` using `~/.ssh/school`.
- `1-create_ssh_key_pair` creates a 4096-bit RSA key pair named `school` and `school.pub`, protected by the passphrase `betty`.
- `2-ssh_config` configures the SSH client to use `~/.ssh/school` and refuse password authentication.

The scripts are intended to run on Ubuntu. Install `2-ssh_config` as `~/.ssh/config` and protect it with mode `600`.

## Task 3

Add the assignment's provided public key to the server user's `~/.ssh/authorized_keys`. This requires the server IP and SSH access to that server; neither was included in the project details provided here.
