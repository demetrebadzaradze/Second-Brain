---
title: Recovering corrupted USB drive
description: I have an USB drive that my friend gave me it is 64 GB drive and USB 2.0 so so nothing crazy but solid. I tested it with validrive and it was pretty slow but truly 64 GB and no error. little did i knew i would have quite some time with it. at first i wanted to mount it on my server but formatting it as FAT32 NTFS or exFAT would not work i would get some errors and nothing else, so i went  with F2FS witch is format made for flash storage and support for it is not much but whatever it worked fine for holding media for my Jellyfin media server until it just started giving I/O error and now i will try to fix.
date: 2025-07-16
draft: false
toc: true
ShowLastmod: true
---


> **WARNING**: STOP USING THE DRIVE IMMEDIATELY IN CASE OF CORRUPTION

## Plan
1. since working with [F2FS](https://docs.kernel.org/filesystems/f2fs.html)(Flash-Friendly File System) Linux is more feasible since it's is supported on there and these tools that i will use are on Linux and are free. for this i will setup a VM(virtual machine) with kali (iso i have but any will do). the tools used here support other popular formats too.
2. download tools or a tool [`testdisk`](https://www.cgsecurity.org/wiki/TestDisk) witch also comes with [`photorec`](https://www.cgsecurity.org/wiki/PhotoRec). powerful and free tools for recovering data.
3. backup the disk image of that corrupted drive so if we screw something up we have a backup or do the recovering on the image while drive is being fixed, but i will be saving that compressed so i wont have to use that much storage.
4. using the tools downloaded, recover the data.

> **_NOTE:_**  if using a VM allocate more then the drive size, for making a backup and recover files allocate double the size of drive you want to recover to make sure you have enough space and wont have to restart 4 times (speaking from experience). for copying on another drive and recovering just Linux plus some space for swap and programs is good enough.

## Backup the raw data of the drive(optional but recommended)
plug in the USB drive or the device you are recovering and do:
```bash
lsblk
```
this lists out all the storage devices accessible(should not be mounted and sizes of drive are sometimes different than what they are branded as). find the one needed and like `sdb` in my case and run the disk image creation command with `dd`:
```bash
sudo dd if=/dev/sdb of=/home/user/backup.img status=progress
```
replace `sdb` and destination on the backup disk image file according to your needs and if you want to compress it run:
```bash
sudo dd if=/dev/sdb status=progress | gzip -c > /home/user/backup.img.gz
```
again  fill in the `sdb` and path for file. destination should have enough.

## Download tool
the tool is `testdisk` soo:
```bash
sudo apt install -y testdisk
```
and doing this this will also downloads the `photorec`.

## Recover data
i will be using `photorec` so just run:
```bash
sudo photorec
```
1. chouse the correct drive(must be plugged in at this point).
2. an then select partition and hot search this will take some time, i waited for 5 hours for 64 GB drive but it will be different for different environments.
3. after it finishes you should have some directories named:
	```bash
	recup_dir.1
	recup_dir.2
	recup_dir.3
	```
	these are recovered files and `photorec` doesn't keeps the folder structure or any names. soo that is on you to fix manually but there are some other ways I'm sure but i want to see what is going on in the there.   



### if you want to recover from image 
do:
```bash
sudo photorec /home/user/backup.img
```
edit path to the drive image wit was dove with [[Recovering corrupted USB drive#Backup the raw data of the drive(optional but recommended)]].

### if its image file is compressed
decompress it first with `gunzip` first and than start `photorec`:
```bash
gunzip /home/user/backup.img.gz
```
enter correct path to file.

## Write back the image to the drive (if wanted)
> **_NOTE_**:  the image will be same so it contains corrupted data

done with `dd` command once again run:
```bash
sudo dd if=/home/user/backup.img of=/dev/sdb bs=4M status=progress
```
- `if=/home/user/backup.img`: Path to your backup image.
- `of=/dev/sdb`: The thumb drive’s device name (not a partition like `/dev/sdb1`).
- `bs=4M`: Block size for faster transfer.
if image is compressed run:
```bash
gunzip -c /home/user/backup.img.gz | sudo dd of=/dev/sdb bs=4M status=progress
```
- `gunzip -c ` : decompresses the image and pipes it to `dd`.

## Fixing the USB
i will still be using the `F2FS` format for this but you are welcome to chouse any that you would like.

so lets try to fix it by installing the tools for this format:
```bash
sudo apt install f2fs-tools
```
and then try to fix it by:
```bash
sudo fsck.f2fs /dev/sdb1
```
change the path accordingly and again use `lsblk` to identify it.

in my case fixing it like this didn't work so i will just reformat it:
```bash
sudo fsck.f2fs /dev/sdb
```
this will delete all data on there but then i will just move recovered files on there and its done.

### Testing USB 
make a folder in `/mnt` directory and mount it on there:
```bash
sudo mkdir /mnt/thumb
sudo mount /dev/sdb /mnt/thumb
```
and this should give no errors and we should be able to read and write on that path and also once we unmount/disconnect all should disappear. 