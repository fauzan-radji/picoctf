# Disk, disk, sleuth!

[Link to the challenge](https://play.picoctf.org/practice/challenge/113)

## Description

Use `srch_strings` from the sleuthkit and some terminal-fu to find a flag in this disk image: [dds1-alpine.flag.img.gz](https://mercury.picoctf.net/static/626ea9c275fbd02dd3451b81f9c5e249/dds1-alpine.flag.img.gz)

## Hints

- Hint 1: Have you ever used `file` to determine what a file was?
- Hint 2: Relevant terminal-fu in picoGym: https://play.picoctf.org/practice/challenge/85
- Hint 3: Mastering this terminal-fu would enable you to find the flag in a single command: https://play.picoctf.org/practice/challenge/48
- Hint 4: Using your own computer, you could use qemu to boot from this disk!

## Solution

First I downloaded the Image file from the link provided. The file was a gzip compressed data, so I used `gzip` to extract it.

```bash
$ gzip -kd dds1-alpine.flag.img.gz
```

After that I use combination of `strings` and `grep` to easily find the flag.

```bash
$ strings dds1-alpine.flag.img | grep picoCTF
  SAY picoCTF{f0r3ns1c4t0r_n30phyt3_a6f4cab5}
```

Boom! There it is.

## Flag

picoCTF{f0r3ns1c4t0r_n30phyt3_a6f4cab5}
