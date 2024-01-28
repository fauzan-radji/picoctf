# Sleuthkit Apprentice

[Link to the challenge](https://play.picoctf.org/practice/challenge/300)

## Description

Download this disk image and find the flag. Note: if you are using the webshell, download and extract the disk image into `/tmp` not your home directory.

- [Download compressed disk image](https://artifacts.picoctf.net/c/137/disk.flag.img.gz)

## Hints

(None)

## Solution

First, of course I downloaded the file using `wget`. The file is a `.gzip` file, so I extracted the file using `gzip` command.

```bash
$ gzip -kd disk.flag.img.gz
```

**\*Note**:

- `-k` option stands for **keep** which means it will keep the input file.
- `-d` option means **decompress** because I want to decompress/extract the file.

After the file is extracted I use `sleuthkit` to investigate the image file. First I need to find where the main partition is.

```bash
$ mmls disk.flag.img
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000206847   0000204800   Linux (0x83)
003:  000:001   0000206848   0000360447   0000153600   Linux Swap / Solaris x86 (0x82)
004:  000:002   0000360448   0000614399   0000253952   Linux (0x83)
```

It looks like the main partition is the fourth one which has **360448** offset. After I know the offset, then I try to look at the directories inside this partition using `fls`.

```bash
$ fls -o 360448 disk.flag.img
d/d 451:	home
d/d 11:	lost+found
d/d 12:	boot
d/d 1985:	etc
d/d 1986:	proc
d/d 1987:	dev
d/d 1988:	tmp
d/d 1989:	lib
d/d 1990:	var
d/d 3969:	usr
d/d 3970:	bin
d/d 1991:	sbin
d/d 1992:	media
d/d 1993:	mnt
d/d 1994:	opt
d/d 1995:	root
d/d 1996:	run
d/d 1997:	srv
d/d 1998:	sys
d/d 2358:	swap
V/V 31745:	$OrphanFiles
```

Well, there is `/home` and `/root` folder there. Let's look at those. First the `/home` directory which has **451** inode.

```bash
$ fls -o 360448 disk.flag.img 451

```

Seems like the `/home` directory is empty. Now lets look at the `/root` directory which has **1995** inode.

```bash
$ fls -o 360448 disk.flag.img 1995
r/r 2363:	.ash_history
d/d 3981:	my_folder
```

There is suspicious folder named `my_folder` there. Lets look at it. **3981** is the inode.

```bash
$ fls -o 360448 disk.flag.img 3981
r/r * 2082(realloc):	flag.txt
r/r 2371:	flag.uni.txt
```

There it is. Using `icat` we can see the content of `flag.uni.txt`.

```bash
$ icat -o 360448 disk.flag.img 2371
picoCTF{by73_5urf3r_adac6cb4}
```

## Flag

picoCTF{by73_5urf3r_adac6cb4}
