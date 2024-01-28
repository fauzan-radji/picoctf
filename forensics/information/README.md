# information

[Link to the challenge](https://play.picoctf.org/practice/challenge/186)

## Description

Files can always be changed in a secret way. Can you find the flag? [cat.jpg](https://mercury.picoctf.net/static/e5825f58ef798fdd1af3f6013592a971/cat.jpg)

## Hints

- Hint 1: Look at the details of the file
- Hint 2: Make sure to submit the flag as picoCTF{XXXXX}

## Solution

first I check the filetype of the file using `file` command.

```bash
$ file cat.jpg

cat.jpg: JPEG image data, JFIF standard 1.02, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 2560x1598, components 3
```

The output is normal, there is nothing wrong with the filetype. After that I try to look at the metadata using `exiftool`.

```
$ exiftool cat.jpg

ExifTool Version Number         : 12.40
File Name                       : cat.jpg
Directory                       : .
File Size                       : 858 KiB
File Modification Date/Time     : 2021:03:16 02:24:46+08:00
File Access Date/Time           : 2023:07:17 22:08:56+08:00
File Inode Change Date/Time     : 2023:07:17 22:08:44+08:00
File Permissions                : -rwxrwxrwx
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.02
Resolution Unit                 : None
X Resolution                    : 1
Y Resolution                    : 1
Current IPTC Digest             : 7a78f3d9cfb1ce42ab5a3aa30573d617
Copyright Notice                : PicoCTF
Application Record Version      : 4
XMP Toolkit                     : Image::ExifTool 10.80
License                         : cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9
Rights                          : PicoCTF
Image Width                     : 2560
Image Height                    : 1598
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 2560x1598
Megapixels                      : 4.1
```

One thing that interesting is the `License` field which is a lil bit suspicious. It looks like a base64 format, so I tried to decode it using `base64`.

```bash
$ echo "cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9" | base64 -d

picoCTF{the_m3tadata_1s_modified}
```

That's it. The flag is **picoCTF{the_m3tadata_1s_modified}**

## Flag

picoCTF{the_m3tadata_1s_modified}
