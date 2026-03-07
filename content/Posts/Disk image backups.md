---
title: Disk images
description: Recently I found myself working with SD cards and thumb drives more often than usual. Reformatting and data recovery and all sorts of related things. Here I will explain how I backup data from storage devices.
date: 2026-03-06
draft: false
toc: true
ShowLastmod: true
---
## Plan
Here how simple **backup** works:
- Make raw `disk image` containing exact bit-by-bit copy of the physical drive.
- Compress it for better storage.

When it comes to **restoring** this data I will just:
-  Decompress the `dick image`.
- Write it to the drive.

Also, I must mention that, You should not always write to disk. instead you could mount the `disc image` as a loop device.

## Make raw disk image
this is commonly done with `dd` command on Linux.
```bash
sudo dd if=/dev/sdx of=random_sdcard_backup.img bs=4M status=progress
```
here `sdx` is the  name of the device. `lsblk` command can be used to list storage devices and their information (e.g. name). 

## Compress disk image
Usually this `.img` file takes up as much storage as the devices storage amount. So compressing it is a good Idea. 
There are lot of compression algorithms and one you choose may vary depending on what kind of information is on the drive and what do you intend to use it for. For example if the data on the drive is already pretty compressed then using better compression algorithms like `xz` would not do a lot, other than take a lot longer.  I found that `gzip` is the  best middle of the ground option. It had been the standard for Linux for decades at this point.
So here is how compression with `gzip` goes:
```bash
gzip random_sdcard_backup.img
```
Here we could use `-k` for the option for keeping the original file. Also `-1, --fast` to compress faster and `-9, --best` to compress better. 


## Decompress disk image
Decompressing is similar we just :
```bash
gunzip random_sdcard_backup.img.gz
```
`-k` can again be used to keep the input file. 

This can also be  done with  `gzip` and `-d` option.

## Write to disk
Now this is the actual writing to disk part and it is done with `dd` command, like this:
```bash
sudo dd if=random_sdcard_backup.img of=/dev/sdX bs=4M status=progress
```
Make sure the device path is correct.

`.img` can also be mounted as a loop device like this:
```bash
sudo mount -o loop random_sdcard_backup.img /mnt/sd-loop
```
make sure destination path exists.
