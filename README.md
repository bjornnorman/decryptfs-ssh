decryptfs-ssh
=============

Solution for automatic decryption of ecryptfs home folders when logging in with SSH keys without password.

# General information

SSH-keys to be used must be both in the users authorized keys and loaded
by ssh-agent for the current session for this script to work properly.

In the examples, the script is placed in /etc/ssh/, but you can put it
wherever you like as long as it is executable by the users logging in with
ssh. Configuration of key files and passphrase wrapper locations is done inside
the script.

# Automation

This script must be run either through the users authorized_keys entry
like or via the ForceCommand option in sshd_config. Examples:

In authorized_keys (for specific users):

    command="/etc/ssh/decryptfs-ssh start" ssh-rsa AA....oJw= user@example.com

In sshd_config (for all users):

    ForceCommand "/etc/ssh/decryptfs-ssh start"

Manual usage:

* Enable automatic decryption for a key:
    decryptfs-ssh enable <user@example.com>

* Decrypt home folder with a specified key:
    decryptfs-ssh decrypt <user@example.com>

* Recrypt folder for the current account:

	decryptfs-ssh recrypt

* Disable automatic decryption for a key:

	decryptfs-ssh disable <user@example.com>
        
# Acknowledgements

This was based on an idea by "kasperd" found in the comments here:

    http://serverfault.com/questions/622344

# Wrap

Let me know what you think and feel free to contribute!

Remember: No warranty and no guarantees... :)
