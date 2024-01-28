# First Find

[Link to the challenge](https://play.picoctf.org/practice/challenge/320)

## Description

Unzip this archive and find the file named 'uber-secret.txt'

- [Download zip file](https://artifacts.picoctf.net/c/501/files.zip)

## Hints

(None)

## Solution

After I downloaded the file using `wget`, I unzip it using `unzip`.

```bash
$ unzip files.zip
```

There's a ton of files and nested directories in the zip file, so I utilize `find` to find specific file with specified filename, in this case **uber-secret.txt**.

```bash
$ cd files
$ find -names uber-secret.txt
./adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/uber-secret.txt
```

The file located at `./adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/uber-secret.txt`. Simply using `cat` command to see the file-content.

```bash
$ cat $(find -name uber-secret.txt)

# OR

$ cd ./adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/
$ cat uber-secret.txt
```

## Flag

picoCTF{f1nd_15_f457_ab443fd1}
