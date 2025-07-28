---
title: Self-Hosted Mumble Voice Server with Docker, Lightweight Discord Alternative
date: 2025-07-28
description: so as of many other blog description i hade a problem, my friend wanted to play some games but his internet is so bad that discord and Minecraft would take up all the bandwidth, witch he found out while experimenting. so i got on it and fount this thing called mumble, self hosted discord but extremely lightweight, here i will be setting that up.
tags:
  - mumble
  - docker
  - self-hosting
  - voice-chat
  - gaming
draft: false
toc: true
ShowLastmod: true
---
Mumble is an open-source, low-latency voice chat system that's perfect for gaming and bad networks. Here's how I deployed it using Docker, plus some fun and useful ways to customize it!

---

## 🐳 Setting Up Mumble in Docker
all of this will be done with docker compose because it the best thing ever.

Here's our simple `docker-compose.yml`:

```yaml
services:
  mumble-server:
    image: mumblevoip/mumble-server:latest
    container_name: mumble-server
    hostname: TG_3w3p
    restart: on-failure
    ports:
      - 64738:64738
      - 64738:64738/udp
    volumes:
      - ./data/:/data
    environment:
      MUMBLE_CONFIG_WELCOMETEXT: "<b>Welcome to TG_3w3p's Mumble!</b><br />Have fun."
      MUMBLE_CONFIG_PORT: 64738
      MUMBLE_CONFIG_USERS: 10
      MUMBLE_CONFIG_SERVERPASSWORD: "password"
      MUMBLE_SUPERUSER_PASSWORD: "admin"
      ```
This runs the official Mumble server image and exposes the necessary ports for voice traffic. All configuration is handled via environment variables or through the mumble_server_config.ini file in ./data. you can see more on this [here](https://github.com/mumble-voip/mumble-docker), documentation is kind of all over soo this is  great start. 
so just run that with :
```bash
sudo docker compose up -d
```
or no `-d` if you want to look at it

****
## 📁 Persistent Data
The `./data` folder stores:
- `mumble_server_config.ini`: Your config file
- `mumble-server.sqlite`: Database for channels, users, etc.

Edit the config manually or let Docker handle it via environment variables.
but in case of editing it manually for me it gets overridden by env variables even if i don't have them configured so add this in the compose file:
```yaml
command: /usr/bin/mumble-server -fg -ini /data/mumble_server_config.ini
```
and this should work but i will stick to the env variables in the compose file. 

****
## ✅ Connect to the Server
Use the [Mumble client](https://www.mumble.info/) and connect using:
- Address: your public IP, LAN IP, or Tailscale IP
- Port: 64738
- Username: anything you want
- Password: password
for me i don't really  have a public IP address but what i have is [Tailscale](https://tailscale.com/) VPN and all i did wat to just share out my server or the device that has `mumble` hosted and they will just use may Tailnet IP and done.

****
## 📜 Custom Banner / Welcome Message
Mumble supports rich HTML in the welcome message:
```env
MUMBLE_CONFIG_WELCOMETEXT: |
  <center><b>🔥 Welcome to TG_3w3p's Mumble 🔥</b><br/>
  <img src=<link> height="100"/><br/>
  Join #Gaming or #Chill rooms to start!</center>

```
and whatever image is on the link will be displayed.

****
## login as `SuperUser`
in the environmental variables we have set the `SuperUser` password witch as the name suggests is like an admin to connect to the server with that, in `username` field you must enter `SuperUser` and this will prompt you to enter super user password that you set in the compose file and you are in. 
once you are a super user you can then manage channels and whatnot

****
## 💡 Ideas for the Future
- add some bots — a channel where no one has voice permission 😄
- Game event channels with custom join sounds
- and it has an API witch can do a lot of things but i won't be using that 

****
## ✅ Final Thoughts
Mumble is an amazing tool — even more so when self-hosted. It's fast, secure, light on resources, and perfect for friends with weak internet who still want to game and chat. With Docker, the setup is incredibly simple, and customization possibilities are endless and add on Tailscale and it can be hosted on anywhere. of course you could make it public but i didn't since it for me and friends but in future i guess

If you're tired of Discord hogging your bandwidth or just want full control, give Mumble a shot!