# Disk, disk, sleuth! II

[Link to the challenge](https://play.picoctf.org/practice/challenge/137)

## Description

All we know is the file with the flag is named `down-at-the-bottom.txt`... Disk image: [dds2-alpine.flag.img.gz](https://mercury.picoctf.net/static/aed64c508175df5fe23207c10e0e47e5/dds2-alpine.flag.img.gz)

## Hints

- Hint 1: The sleuthkit has some great tools for this challenge as well.
- Hint 2: Sleuthkit docs here are so helpful: [TSK Tool Overview](http://wiki.sleuthkit.org/index.php?title=TSK_Tool_Overview)
- Hint 3: This disk can also be booted with qemu!

## Solution

First, I downloaded the file.

```bash
$ wget https://mercury.picoctf.net/static/aed64c508175df5fe23207c10e0e47e5/dds2-alpine.flag.img.gz
```

Then I extract it using `gzip` with `-dk` option to **decompress** and **keep** the input file.

```bash
$ gzip -kd dds2-alpine.flag.img.gz
```

After that, I use `sleuthkit mmls` to display the layout of this disk, and here's what I found:

```bash
$ mmls dds2-alpine.flag.img
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000262143   0000260096   Linux (0x83)
```

The offset of the partition is **2048**. So I use `fls` to list the directories and found `/home` and `/root` directory there.

```bash
$ fls -o 2048 dds2-alpine.flag.img
d/d 26417:	home
d/d 11:	lost+found
r/r 12:	.dockerenv
d/d 20321:	bin
d/d 4065:	boot
d/d 6097:	dev
d/d 2033:	etc
d/d 8129:	lib
d/d 14225:	media
d/d 16257:	mnt
d/d 18289:	opt
d/d 16258:	proc
d/d 18290:	root
d/d 16259:	run
d/d 18292:	sbin
d/d 12222:	srv
d/d 16260:	sys
d/d 18369:	tmp
d/d 12223:	usr
d/d 14229:	var
V/V 32513:	$OrphanFiles
```

Then using the `fls` again to look inside the `/home` (which has **26417** inode) and found nothing. Then I look for to the `/root` content (inode **18290**).

```bash
$ fls -o 2048 dds2-alpine.flag.img 26417
$ fls -o 2048 dds2-alpine.flag.img 18290
r/r 18291:	down-at-the-bottom.txt
```

There the file is. Now we already know where the file is, lets look at the content of the file.

```bash
$ icat -o 2048 dds2-alpine.flag.img 18291
   _     _     _     _     _     _     _     _     _     _     _     _     _
  / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \
 ( p ) ( i ) ( c ) ( o ) ( C ) ( T ) ( F ) ( { ) ( f ) ( 0 ) ( r ) ( 3 ) ( n )
  \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/
   _     _     _     _     _     _     _     _     _     _     _     _     _
  / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \
 ( s ) ( 1 ) ( c ) ( 4 ) ( t ) ( 0 ) ( r ) ( _ ) ( n ) ( 0 ) ( v ) ( 1 ) ( c )
  \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/
   _     _     _     _     _     _     _     _     _     _     _
  / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \
 ( 3 ) ( _ ) ( f ) ( 5 ) ( 5 ) ( 6 ) ( 5 ) ( e ) ( 7 ) ( b ) ( } )
  \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/
```

There the flag is, but I need to extract that first. I can spend 5 minutes to do it manually or spend 5 hours to make it automatic. So, as a programmer I use **javascript** to make it automatic :sunglasses: (It doesn't take 5 hours tho).

```javascript
`
   _     _     _     _     _     _     _     _     _     _     _     _     _  
  / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \ 
 ( p ) ( i ) ( c ) ( o ) ( C ) ( T ) ( F ) ( { ) ( f ) ( 0 ) ( r ) ( 3 ) ( n )
  \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/ 
   _     _     _     _     _     _     _     _     _     _     _     _     _  
  / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \ 
 ( s ) ( 1 ) ( c ) ( 4 ) ( t ) ( 0 ) ( r ) ( _ ) ( n ) ( 0 ) ( v ) ( 1 ) ( c )
  \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/ 
   _     _     _     _     _     _     _     _     _     _     _  
  / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \ 
 ( 3 ) ( _ ) ( f ) ( 5 ) ( 5 ) ( 6 ) ( 5 ) ( e ) ( 7 ) ( b ) ( } )
  \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/ 
`
  .match(/\( [\w{}] \)/gi)
  .map((c) => c.slice(2, 3))
  .join("");
```

I ran that code in the browser console and get the flag extracted.

## Flag

picoCTF{f0r3ns1c4t0r_n0v1c3_f5565e7b}
