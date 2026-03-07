---
title: New Terraria server
description: Updating existing Terraria server from vanilla containerized server (not even using the compose file) to more professional server using `TShock`, open source software for more control over the server.
date: 2025-12-04
draft: false
toc: true
ShowLastmod: true
---
## Intro

I already had a [Terraria server](https://demetrebadzaradze.github.io/Second-Brain/posts/host-terraria-server-on-linux-server/) set up that I used for a while. But once I came back, I saw a lot of flaws with my previous setup, mainly performance, and not enough customization. So I searched and found this project called [TShock.](https://github.com/Pryaxis/TShock/ ) It is great, and in short, it tweaks a lot of things that are public in the Terraria source code. It also makes a lot of things much better like world saving, administration and it is structurally better than junk I had before.

## Plan
Plan is to have a **TShock** powered terraria server as a container, make it easily runnable and also migrate to it. 

## Docker compose set-up
This time i will  be using `docker compose`, since it is easy to configure one `.yml` file once and than just compose it up and down, rather than figuring out want environment variable need to be based in a docker run command, every time I start the server. Plus this way I can make server start automatically after boot.

Here is what the `compose.yml` file looks like:
```yaml
services:
  terraria:
    image: ghcr.io/pryaxis/tshock:latest
    container_name: terraria-test
    volumes:
      - "./tshock/:/tshock"
      - "./worlds:/worlds"
      - "./plugins:/plugins"
      - "/etc/localtime:/etc/localtime:ro"
    ports:
      - "7777:7777"
#    command: -world /worlds/<world name>.wld
    restart: "no"
    stop_grace_period: 60s
    tty: true
    stdin_open: true
```
`restart` can be set to `unless-stopped` so it starts on boot.
> **NOTE:** `command` option is commented because initial run of the container is just needed to create the world. After that this option needs to be uncommented and world name needs to be entered appropriately (replacing `<`, `>` and content in the middle).  

## Running the server
Now this can be ran in two ways. 

1.   First is the interactive way with this:
```bash
docker compose run terraria
```
>**NOTE:** Here `terraria` is the name of the service that is defined in the `.yml` file. So replace it accordingly.

2. And none interactive way with:
```bash
docker compose up
```
This just gives read only logs of the container. You can also run this in detached mode with `-d` option. This way is simpler and preferred if you are not going to use any commands on not interact with the program, it is great for just running it.

### First run
Upon first boot, if you don't have the world created and entered in the  `.yml`, you will have to create the world. This is an interactive process so run with `run` command instead of `up` and follow the world configuration steps.

### After first run
After initial run world should be created in the appropriate directory (`./worlds`, on host, in this case) with the name you chouse, as a `.wld` file. Then uncomment the the `command` option in `.yml` file and configure whatever you wish. And finally run it as you wish.

## Migrating from old set-up to TShock
All we need is a `.wld` file from the old set-up. Place that into `./worlds` directory (optional, since you can just mount the old path for `/worlds` directory, but clean), uncomment `command` option in the `.yml` and  input the appropriate path to this world. 

You can then follow the TShock guidance in the chat and finish the setup and then configure the server as you wish.   
