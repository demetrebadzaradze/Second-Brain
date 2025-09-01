---
title: Setting up PI-Hole
description: Are you also tired of ads, I certainly am so don't i get the network wide ad blocker like  PI-Hole. It looks like a  cool piece of software and i kind of want an ad blocker and it will be better if its network wide thing and added my VPN its a strong combo despite my CG-NAT limitations 
date: 2025-09-01
draft: false
toc: true
ShowLastmod: true
---
## My setup
Currently I have small low end server witch is behind a `CG-NAT`, but I have a VPN so this ad blocker should work if I'm away.
Also i want it as a container, so I will use [pi-hole docker version](https://github.com/pi-hole/docker-pi-hole). Reason why I went for container is little influenced by [this](https://github.com/mrjackwills/oxker) project. It is really cool, it displays docker containers and logs and info about them in a terminal.    

****

## Plan
1. Read the docs and get familiar with the tool
2. Install it on the server
3. Update per device DNS settings or the router DNS settings

****

## Docs and helpful information
[pi-hole website](https://pi-hole.net/)
[pi-hole docs website](https://docs.pi-hole.net/)
[Linus's video about pi-hole](https://www.youtube.com/watch?v=KBXTnrD_Zs4)
[pi-hole Github](https://github.com/pi-hole)

****

## Installation on the server
Install as container is pretty simple from [this repo](https://github.com/pi-hole/docker-pi-hole) as they have nice compose file in a [Readme](https://github.com/pi-hole/docker-pi-hole/blob/master/README.md#quick-start). But it will not work for my setup, Because my DNS, HTTPS and HTTP ports are already in use. HTTP/HTTPS in no problem but DNS ports are different. I don't want to stop one that's in use already so my `compose.yml` file looks like this:
```yaml
services:
  pihole:
    container_name: pihole
    image: pihole/pihole:latest
    ports:
      - "53:53/tcp"
      - "53:53/udp"
      - "9000:80/tcp"
      - "9443:443/tcp"
    environment:
      TZ: 'Etc/GMT'
      FTLCONF_webserver_api_password: 'ExTrAeXtRa__STRONG__PaSsWoRd'
      FTLCONF_dns_listeningMode: 'all'
    volumes:
      - './etc-pihole:/etc/pihole'
    cap_add:
      - SYS_NICE
    restart: unless-stopped
```

****

## Making Pi-hole host use Pi-hole
and since I'm on ubuntu server i still need some modifications, like adding this:
```conf
static domain_name_servers=127.0.0.1
```
to this file `/etc/dhcpcd.conf`.
And also stopping and disabling `systemd-resolved.service` service:
```bash
sudo systemctl stop systemd-resolved.service
sudo systemctl disable systemd-resolved.service
```
 and make sure that inside `/etc/resolv.conf` `nameserver` is not something local set it to google as DNS provider:
```conf
nameserver=8.8.8.8
```

****

## Making your network take advantage of Pi-hole
So here we need to configure router to use my servers pi-hole as DNS server and the app will block malicious sites, ads and unwanted sites.
Each router is different but generally its under `Advanced > IP Adrresing > DHCP Settings`. there are many docs for understanding this further like [here](https://docs.pi-hole.net/main/post-install/#making-your-network-take-advantage-of-pi-hole) 

****

## Accessing web UI of Pi-Hole
The settings and whole dashboard is web based so go to your server's IP address and application's port and enter the password for login. If you didn't set the password it will generate a random one and print that in logs, be sure to change it afterwards. after that you have full accesses to this powerful application.    