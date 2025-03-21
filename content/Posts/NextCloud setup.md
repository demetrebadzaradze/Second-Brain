---
title: NextCloud setup
description: Nextcloud is google drive if cloud was your server. at least thats wht i will be using for because i have a 500GB hardrive and im lacking storage on my devices.   
date: 2025-03-18
draft: false
toc: true
ShowLastmod: true
tags:
  - HomeServer
  - LocalCloud
  - ubuntu
  - linux
---

## What is NextCloud?
[Nextcloud](https://nextcloud.com/) is a opensource self hosted app for data storage and here i will be using it for my home server because i am running out of storage on my devices and i have this 500GB Hardrive that is not in use for now so this project solves many problems.  

## PLAN
follow this official [repo](https://github.com/nextcloud/all-in-one#nextcloud-all-in-one) for docker installation(because docker is pure magic) and 

## Setup
to get this app started make `compose.yml` file and fill in like this:
```yml
---
services:
  nextcloud:
    image: lscr.io/linuxserver/nextcloud:latest
    container_name: nextcloud
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Etc/UTC
    volumes:
      - /path/to/nextcloud/config:/config
      - /path/to/data:/data
    ports:
      - 443:443
    restart: unless-stopped
```
of course you can change the machine port and directories accordingly.
- `data` is folder where all of the files and folders will be saved 
- `config` is self explanatory
- `port` is the port on witch app  will be ran on.
- change the `TZ` time zone 
- also change `puid` and `pgid` for your user. to check your ids type `id` in terminal
[more](https://docs.linuxserver.io/images/docker-nextcloud/#parameters) for this step

after that run 
```bash 
sudo docker compose up -d
```
in a same directory as the compose file and after successful run 👇👇👇 
## Login
1. go on that website it should be `https://<ip-addres-or-name-of-host>:<port>`
2. make new admin account
3. and you are done.

## more things you can do 
I will use their phone app and and tailscale VPN for more accessibility.

## manually Installing docker compose
for server I need docker compose plugin. [here](https://docs.docker.com/compose/install/linux/) is how to to install it but basically its:
1. making a variable:
```bash
DOCKER_CONFIG=${DOCKER_CONFIG:-$HOME/.docker}
```
2. making a directory for installation:
```bash
mkdir -p $DOCKER_CONFIG/cli-plugins
```
3. and getting the binary:
```bash
curl -SL https://github.com/docker/compose/releases/download/v2.34.0/docker-compose-linux-x86_64 -o $DOCKER_CONFIG/cli-plugins/docker-compose
```
4. and executing it 
```bash
chmod +x $DOCKER_CONFIG/cli-plugins/docker-compose
```

so now I have docker compose as plugin:
```bash
docker compose version
Docker Compose version v2.34.0
```

but remember this is for the one user you are logged in as. for all users checkout [this](https://docs.docker.com/compose/install/linux/) 