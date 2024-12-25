---
title: Host terraria server on Linux server
date: 2024-12-22
toc : true
ShowLastmod : true
---

**easiest and simplest way** to do this is to run it on [docker](https://www.youtube.com/watch?v=oUnWU4Y4kSY), because docker is pure magic and there docker image that handles all of what this needs called `rathena/terraria`.

## installing docker 
update repos:
```bash
sudo apt update 
```
then install docker:
```bash
sudo apt install -y docker.io
```
and enable sysctl:
```bash
sudo systemctl enable --now docker
```

## pull and run image
probably making new directory for server configs is a good idea:
```bash
mkdir ~/opt/terraria/server1
```
or something like in games directory what ever you would like just be careful with perditions.

- ### pull the image
	```bash
	docker pull rathena/terraria
	```
- ### run the server
	```bash
	docker run -d \
  --name=terraria-server \
  -p 7777:7777 \
  -v ~/opt/terraria/server1:/config \
  -e WORLD_NAME="MyWorld" \
  -e MAX_PLAYERS=10 \
  -e DIFFICULTY=2 \
  --restart unless-stopped \
  rathena/terraria
	```
	now here there might be some **things to modify**
	- `--name` is a name of container this will be used for starting and stopping it if you forget run `docker ps`
	- `-p` shows witch ports to forward from container to real machine and `7777` is a default port for terraria server. if you are running more then one definitely change this. if not this is good.

	- `-v` binds `/configs` folder on container to `~/opt/terraria/server1` on our server witch we initially crated, if you want to bind it somewhere else just change the `~/opt/terraria/server1` part to your desired path and again be careful with permeations.
	- `-e` makes environmental variables to configure server and thy are pretty self explanatory. 
		1. `WORD_NAME` specifies name of the world.
		2.  `MAX_PLAYERS` specifies max player count.
		3.  `DIFFICULTY` specifies difficulty of the game like
			- `0`: Normal
			- `1`: Expert
			- `2`: Master
			- `3`: Journey Mode
		change as you wish.
		1.  **some other useful environmental variables** are:
			- `-e PASSWORD="yourpassword"` specifies password for the server
			- `-e SEED="worldseed"`: Specifies a seed for world generation.
			- `-e PORT=7777`: Sets the server's port. again if you are running another server change the port witch it runs on here and port forwarded in `-p` flag
		1.  `--restart unless-stopped` this ensures that after power out of restart or shut down server starts automatically if you don't want that, delete it.
		2. and `  rathena/terraria` this you don't want to change, its a docker image witch container is created from.
## managing server
now at this point server is running and here are some useful command:
- **Stop the server**: `docker stop terraria-server`
- **Start the server**: `docker start terraria-server`
- **Check logs**: `docker logs -f terraria-server`
if its called different name check with `docker ps`

## accessing the server
now for me I'm using [tailscale](https://tailscale.com/) witch is kind like a [VPN](https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-vpn) and works behind [CG-NAT](https://nfware.com/blog/what-is-the-difference-between-nat-and-cgnat) witch is my problem too, but its solved and for me and my friend it will work just fine, all they need to do is use my server as they exit node turn the connection on and write in its tailscale IP and then port.

### if you are not using tailscale
this is not recommended but you forward your server's terraria's port and then share your public IP address to people that want to join and port. this doesn't work for CG-NAT. 

[how to forward ports on your router?](https://nordvpn.com/blog/open-ports-on-router/)

## And if you are thief and have a cracked version of Terraria (or friend has)
**first off all that violates Terraria's terms of service and if you can you should 100% support the developer and get the real licensed version. allowing cracked users  also is a bit risky because those users also bypass security checks.**

but if your friend is cheap and won't buy it :
1. locate the `serverconfig.txt` file, for us it will be here `~/opt/terraria/server1/serverconfig.txt` and open it up with some text editor:
	```bash
	nano ~/opt/terraria/server1/serverconfig.txt
	```
1. and change `ValidateSteam=` from `true` to `false`
2. and restart the container:
	```bash
	docker restart terraria-server
	```
and it should work now for cracked players.