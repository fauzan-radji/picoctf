# Big Zip

[Link to the challenge](https://play.picoctf.org/practice/challenge/322)

## Description

Unzip this archive and find the flag.

- [Download zip file](https://artifacts.picoctf.net/c/505/big-zip-files.zip)

## Hints

- Hint 1: Can grep be instructed to look at every file in a directory and its subdirectories?

## Solution

Firstly, after downloaded the file I unzip it using `unzip`.

```bash
$ unzip big-zip-files.zip
```

There are many files and nested directories inside the zip so it would take a long time to search the flag manually. Fortunately we have `grep` to search specific string inside files, and we can do it recursively, meaning we can search through hundred of files and nested directories for the string.

```bash
$ grep "picoCTF" -r
```

Notice I use the `-r` option to search recursively. In a matter of second the flag is found inside this file `folder_pmbymkjcya/folder_cawigcwvgv/folder_ltdayfmktr/folder_fnpfclfyee/whzxrpivpqld.txt`

## Flag

picoCTF{gr3p_15_m4g1c_ef8790dc}
