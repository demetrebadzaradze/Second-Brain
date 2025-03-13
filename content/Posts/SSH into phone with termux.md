---
title: SSH into phone with termux
description: pretty simple setup, works in private network and such and phone doesn't needs to be rooted
date: 2025-01-20
draft: false
toc: true
ShowLastmod: true
---
## Plan
have [termux](https://github.com/termux/termux-app) on phone and we are going to get the IP, username and password and then run the server on termux and connect to if from phone.

### get the local IP of phone
for this run:
```bash
pkg install iproute2
ip a
```
and get `wlan0` IP or something similar like `wlan1` if phone is using Wi-Fi.

### get the username
username is simplest. you just run:
```bash
whoami
```
pretty self-explanatory and it will output username.

### get password
the password is for logging in and you probably don't have it set, so run:
```bash 
passwd
```
and set it.

### start SSH server
first download `openssh` package:
```bash
pkg install openssh
```
and then run the server:
```bash 
sshd
```
also you can run `sshd &` if you want ssh server to keep running in the background after closing termux. 

### connect to phone 
to connect to that phone run:
```bash
ssh -p 8022 <username>@<phone IP>
```
`-p` specifies the port for connection and `8022` is default on phone I think.  