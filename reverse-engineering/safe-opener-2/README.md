# Safe Opener 2

## Description

What can you do with this file?\
I forgot the key to my safe but this [file](https://artifacts.picoctf.net/c/289/SafeOpener.class) is supposed to help me with retrieving the lost key. Can you help me unlock my safe?

## Hints

- Hint 1: Download and try to decompile the file.

## Solution

The file is a java class file. I simply use strings to get readable strings from the file and grep for filter out the flag.

```bash
$ strings SafeOpener.class | grep picoCTF
,picoCTF{SAf3_0p3n3rr_y0u_solv3d_it_de45efd6}
```

## Flag

picoCTF{SAf3_0p3n3rr_y0u_solv3d_it_de45efd6}
