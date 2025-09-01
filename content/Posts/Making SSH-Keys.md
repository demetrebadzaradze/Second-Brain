---
title: Making SSH-Keys
description: Here i will be setting up ssh keys for my server. because I'm tired of entering my password aggain and aggain and aggain. also it is more secure.
date: 2025-08-16
draft: false
toc: true
ShowLastmod: true
---

## What are SSH Keys
Normally if one needs to connect to a remote server/machine they would use `secure shell (SSH)`, this is a go to way, it is secure as the name implies but it is not protected against brute force attacks. SSH keys does something different to get you connected. it makes keys one for client (private) and one for server (public). once you share the public one to the server, it sends 'puzzle' based on that public key to you and if your private key can solve that than you are authenticated. so it is basically a if server and client have valid key pair than it lets you in.    
## Plan
1. Make a key pair (public and private). 
2. Share public key to the server and test it out. 
3. Optionally disable password login, to make it actualy safe agganst brut force attacks. 

## Making key pair
> **_NOTE:_** `SSH` is installed on `Windows` `mac OS` and most `Linux's` by default and it will be needed off course.

Key gen is is pretty simple command:
```bash
ssh-keygen
```
- It will ask for a file name for keys and generally you would only change the name of it not the path. keep it in`.ssh` folder. it makes key with default name if input is empty. could use that but naming it better practice.
- It also will ask for a `passphrase` which is an extra layer of protection and is recommended to set but could be done with this empty too. 
- This command then saves two files with the name you entered that's private key and one with same name but `.pub` extension. the public key.
- And output of this command should look like this:
	```bash
	C:\Users\user>ssh-keygen
	Generating public/private ed25519 key pair.
	Enter file in which to save the key (C:\Users\user/.ssh/id_ed25519): test
	Enter passphrase (empty for no passphrase):
	Enter same passphrase again:
	Your identification has been saved in test
	Your public key has been saved in test.pub
	The key fingerprint is:
	SHA256:********/******+****+****/*/************ user@host
	The keys randomart image is:
	+--[ED25519 256]--+
	|          +      |
	|         . E     |
	|        .   .    |
	|     . . o      .|
	|      = S +    ..|
	|       = + o o +.|
	|  .     o = BoTm |
	|   .     + X +BX+|
	|     .    o *e$@+|
	+----[SHA256]-----+
	```

## Share public key to server
The server should have a `~/.ssh/authorized_keys` file (if not make it) and your public key (the contents of the generated file that has .pub extension) should be copied there as new line.

All of this is is easily done with this command: 
```bash
ssh-copy-id -i <path to your public key file> <username for server>@<server ip or domain name>
```

But sometimes `ssh-copy-id` command is not available by default especially on Windows so you need do all of what that command does manually like this:
```bash
cat <path to public key file> | ssh <server username>@<server ip or domain> "mkdir -p ~/.ssh && chmod 700 ~/.ssh && cat >> ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys"
```
Or from Windows replace first host `cat` command to `type` like this:
```bash
type <path to public key file> | ssh user@your-server "mkdir -p ~/.ssh && chmod 700 ~/.ssh && cat >> ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys"
```

Or just do it manually. (what i did) 

### Testing
To test if this works you just try  to connect to server:
```bash
ssh <username>@<server ip or domain>
```
and it should not ask for password.

## Disable password login
At this point if you just want to do an auto login this is not required, as you see in testing, but if you want users to only connect with keys you add as an administrator and make server more secure, then disable password based login.

The configuration for `SSH` as server is mostly at `/etc/ssh/sshd_config` but in some OS's its different and some Linux distros handle it differently so do a small research about that. after SSH config file is  located just edit that:
```bash
sudo nano /etc/ssh/sshd_config
```

and change some settings like:
- `PermitRootLogin` to `no` - this allows users to login as Root. and we are disabling that with `no`.
- `PasswordAuthentication` to `no` - this will disable password authentication.
- `PermitEmptyPasswords` to `no` - so empty passwords cant come in.
- `Use PAM` to `no`
also could use 
- `AuthenticationMethod` to `publickey` - this sets public key as only Authentication method.
- `AllowUsers` to users you want to to be able to connect with `SSH`
so apply ones that you want.

and restart `ssh` services with:
```bash
sudo systemctl restart ssh
```
