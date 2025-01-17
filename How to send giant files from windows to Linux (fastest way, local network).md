---
title: How to send giant files from windows to Linux (fastest way, local network)
description: of course it is not fastest for everyone but i only use one thing that needs downloading, python, to host and on Linux wget to receive it
date: 2025-01-17
draft: false
toc: true
ShowLastmod: true
---
## How to send giant files from windows to Linux (fastest way, local network)
I needed to sent some files to my server and I was on same network and fastest would probably be to transfer it via cable or something but the private network is also fast

## Plan
### **On windows** 
have [python](https://www.python.org/downloads/), you probably have that too.
and then host target folder with `cmd`. go to path file is located in:
```bash
cd /path/to/directory/file is located/in
```
run server with python:
```bash
python -m http.server 8000    
```
and also get the IP of that machine to find file
```bash
ipconfig 
```
this will display network adapters and search for one you are using and get `IPv4 Address`.

### **on Linux** 
navigate to directory for download to go in and run:
```bash 
wget http://<widnsows IP>:8000/<file-name-with-extention>
```
and the wait.

### note 
this might not work bc windows blocks any kind of incoming network for http and also ping. so what i did was go in **windows security>firewall & network protection** and turn of whichever has your network name in active networks list **temporally**.for me it was public one but it can be private too. and after download turn all of that on again to be protected.   

and on classics programmer fashion  i wasted more time figuring all of this out then if i just uploaded it do cloud or something, but i hope there should be no error for  you and this will be fastest. 