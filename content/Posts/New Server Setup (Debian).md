---
title: New Server Setup (Debian)
description: Giving second life to another old laptop. This one has an SATA port with I populated with 256GB SSD also has an intel atom x5-E8000 CPU @ 1.04GHz 4 cores and 4GB of RAM. Dedicated for running Nextcloud and maybe pihole
date: 2025-10-05
draft: false
toc: true
ShowLastmod: true
tags:
  - HomeServer
  - LocalCloud
  - Debian
  - linux
---
## Plan
plan is extremally simple:
1. Install Debian on server.
2. Install the media Drive.
3. Install Nextcloud and monitoring/displaying software to make it all pretty.

****
## Debian Install
This step i thought would take somewhere around a hour but i was stuck here for **3 days**. the thing was that i didn't had beefy enough USB drive, but as always i would realize that far into the project, after i would try every possible configuration starting from Rufus all the way to the custom made ISOs, but nothing worked other than **most bizarre solution**:
1. Install Arch(BTW) on a USB drive since it is so lite.
2. Get Arch running.
3. Install the media SSD.
4. mount the internal storage, since live USB has limited storage.
5. Install and flash Debian ISO in media Drive.
6. Boot from that drive and install Debian.
and i had that working just fine, other than some packages straight up not working.

****
## Configuration 
Coming from Ubuntu server Debian is not as defaulted in terms of configurations, even the aliases are commented out so there was a a plenty things to setup way i like it. 
#### `sudo` and `su`
Also no `sudo` by default, witch was surprising until i found out the reason, that `sudo` is just `su` do, so telling the superuser to do one thing and for authorization it uses the current users password. so using `su` is better for security and I'm getting along with it quite nicely.

#### `.bashrc`
Also I wanted this server to resemble the Debian setup that i have in `termux` on my phone so kind of like a station so had to display some ASCII art,`fastfetch` and `micro` instead of `nano`. Custom `PS1`, but nothing fancy just red colored `root` for super user and green for others.
  
****

## Software Install

### Monitoring/Always On Display
This new `top` child called [btop](https://github.com/aristocratos/btop/tree/v1.4.5) looks cool and is actually useful and feature dense and just look at [it](https://github.com/aristocratos/btop/tree/v1.4.5?tab=readme-ov-file#screenshots):
![beautiful btop screenshot](https://screenshots.debian.net/screenshot/btop/22650)
this one is not mine though, but i will be experimenting with it and the themes look so good too.

for monitoring i will be using `btop` looks nice and is displaying some useful general info that i need.



### Nextcloud setup
Easiest way to run Nextcloud is with container, but since I'm using `btop` i want to monitor everything separately and not as one docker program for example, so i will be installing it manually, following the [official manual](https://docs.nextcloud.com/server/stable/admin_manual/installation/source_installation.html#) witch uses [LAMP Stack](https://www.ibm.com/think/topics/lamp-stack).

#### PHP Install
Recommended PHP version, for now, is `v8.3` and in Debian repos there is only the newest version that can be installed like this:
```bash
apt install -y php libapache2-mod-php php-mysql php-mbstring
```
so for specific version, i added sury.org repository:
first install tools, get the sign and add repo:
```bash
apt install -y apt-transport-https lsb-release ca-certificates curl
curl -sSLo /usr/share/keyrings/deb.sury.org-php.gpg https://packages.sury.org/php/apt.gpg 
echo "deb [signed-by=/usr/share/keyrings/deb.sury.org-php.gpg] https://packages.sury.org/php/ $(lsb_release -sc) main" | tee /etc/apt/sources.list.d/php.list 
```
update `apt` repos
```bash
apt update
```

and now install specific versions
```bash
apt install php8.3 libapache2-mod-php8.3 php8.3-mysql php8.3-mbstring
```

##### test PHP
First check the version to see if its even installed:
```bash
php -v
```
Then add new `php` file in `apache` directory with your editor of choice:
```
micro /var/www/html/test.php
```
and add test PHP code like:
```php
<?php
phpinfo();
?>
```
save the changes.
then restart `apache2`
```bash
systemctl restart apache2
```
and from browser navigate to the newly added page `http://<Server's IP>/test.php/` and here should be the information about `php`, meaning it is in working state.

##### Installing required PHP extensions
Nextcloud needs some extensions to work as intended:
```bash
apt install -y php php-mysql php-gd php-xml php-mbstring php-curl php-zip php-intl php-bcmath php-gmp libapache2-mod-php unzip wget
```
or the specific versions of this.

#### MariaDB Install
MariaDB is is the suggested database for Nextcloud so i installed it:
```bash
apt install -y mariadb-server mariadb-client
```
start and enable it:
```bash
systemctl start mariadb && systemctl enable mariadb
systemctl status mariadb
```
and status should be active.

and now to secure it run a script named `mariadb-secure-installation`
```bash
mariadb-secure-installation
```
and follow the installation, set root password, remove anonymous users so only set users can login, disallow remote root login for security reasons, remove unnecessary test database and reload the privilege table.

##### Create Database For Nextcloud
`mariadb` is drop in replacement for `mysql`, also a fork of it and developed my same guy so both of them will work.
log into the `mariadb` database as root with password you set in last step:
```bash
mariadb -uroot -p
```
and from there create database:
```sql
CREATE DATABASE <database name>;
```
-  Replace `<database name>` with actual name for your database (e.g. `nextcloud_db`). This is needed for Initial setup of Nextcloud. 
Create new user for Nextcloud to use:
```sql
CREATE USER <database username>@localhost IDENTIFIED BY '<password for this user>';  
```
- Replace `<database username>` with actual  username and `<password for this user>` withe secure password for that user, these will also be needed for initial setup of Nextcloud. 'localhost' is used since the Nextcloud and the database are  on the same server.  
Give permissions for the database to user, both of witch we just made in an earlier steps. 
```sql
GRANT ALL PRIVILEGES ON <database name>.* TO <database username>@localhost;
```
and flush the privileges and exit:
```sql
FLUSH PRIVILEGES;
EXIT
```

#### Apache2 Install
[Apache2] is for  actual serving webpages to the servers IP address or domain. 

Debian 13 didn't had this installed by default so:
```bash
apt install -y apache2
```
then start and enable it:
```bash
systemctl start apache2 && systemctl enable apache2
systemctl status apache2
```
And visiting the `http://<Servers IP>` should display the default `apache2` page for Debian after firewall is configured.

##### Firewall configuration 
configuring the  firewall is critical part of this for security and for it to work properly.
so i installed `ufw` (Uncomplicated Firewall) witch is a frontend for `iptables` or `nftables`, making it easier to manage rules without complex syntax. 
Install:
```bash
apt install -y ufw
```
and configured to enable incoming http and https requests, loopback, witch is a virtual interface `lo` and is used for local services to communicate and not use the external interfaces like `wlan0` or `eth0`, and also SSH connections:
```bash
ufw enable
ufw status
ufw allow ssh
ufw allow http
ufw allow https
ufw allow in on lo
ufw reload
ufw status
```
and as a result I got:
```bash
Status: active

To                         Action      From
--                         ------      ----
22/tcp                     ALLOW       Anywhere
80/tcp                     ALLOW       Anywhere
443                        ALLOW       Anywhere
Anywhere on lo             ALLOW       Anywhere
22/tcp (v6)                ALLOW       Anywhere (v6)
80/tcp (v6)                ALLOW       Anywhere (v6)
443 (v6)                   ALLOW       Anywhere (v6)
Anywhere (v6) on lo        ALLOW       Anywhere (v6)
```

#####  Apache2 Configuration
First change the working directory to where `apache2` serving files are located at:
```bash
cd /var/www/html/
```
Get the latest version of Nextcloud from the official website and unzip and delete it:
```bash
wget https://download.nextcloud.com/server/releases/latest.zip
unzip latest.zip
rm -f latest.zip
```
correct the ownership and permissions so Apache can access the unzipped folder `nextcloud`:
```bash
chown -R www-data:www-data nextcloud/
chmod -R 755 nextcloud/
ls -l
```
list should show this:
```bash
drwxr-xr-x 14 www-data www-data  4096 Sep 27 11:55 nextcloud
```
Then i added single configuration file. for Debian it should in this path:
```bash
micro /etc/apache2/sites-available/nextcloud.conf
```
and insert this content:
```conf
<VirtualHost *:80>
  DocumentRoot /var/www/html/nextcloud/
  DocumentRoot  192.168.1.10
  
  <Directory /var/www/html/nextcloud/>
    Require all granted
    AllowOverride All
    Options FollowSymLinks MultiViews
  
  <IfModule mod_dav.c>
      Dav off
    </IfModule>
  </Directory>
</VirtualHost>
```
and replace `DocumentRoot`, `DocumentRoot` and `Directory` according to your setup but this works for this documentation.
To enable the site run:
```bash
a2ensite nextcloud.conf
```
Enable additional modules:
```bash
a2enmod rewrite headers mime env dir
```
And restart Apache to apply changes: 
```bash
systemctl restart apache2
```

#### Web interface setup
On browser go to the domain name or the IP of the server. The first Time visit asks for configuration like **admin username and password**. Also **Data folder**, this is where data is saved at and by default it is set to the same directory were app is server from + `/data`. setting custom path is simple:
```bash
mkdir nextcloud
chown -R www-data:www-data nextcloud/
chmod -R 700 nextcloud/
ls -l
```
this could be ran everywhere and gives correct, permissions:
```bash
drwx------ 2 www-data www-data  4096 Oct 12 15:29 nextcloud
```
and also `.ncdata` file should be present in the data folder:
```bash
micro ./nextcloud/.ncdata
```
and it should have this:
```
# Nextcloud data directory
```

And fill in the database information from previous steps and hit install.

##### CLI only install
For me web UI didn't work so i changed directory to the Nextcloud and ran this:
```bash
php occ  maintenance:install  --database '<mysql>' --database-name '<database name>'  --d
atabase-user '<database user>' --database-pass '<data base user password>'  --admin-user '<admin name>' --admin-pass '<admin password>'
```
replace the items that are like this `< >`.after install edit the `config/config.php` to adjust some desired setting like trusted domains and data folder path(this still needs `.mcdata` file in there with same `# Nextcloud data directory` content) after that reapply all the permissions to all Nextcloud directories and all set.

****

## Finish
Now that all of this is done I will be adding users to Nextcloud and make it usable for  other at my house and maybe if specs help me i will move this to different port and also run PIHole on here too.  
