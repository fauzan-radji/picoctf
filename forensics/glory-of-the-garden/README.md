# Glory of the Garden

## Description

This garden contains more than it seems.

## Hints

- Hint 1: What is a hex editor?

## Solution

First I check the filetype although it's a `.jpg` file just in case.

```bash
$ file garden.jpg

garden.jpg: JPEG image data, JFIF standard 1.01, resolution (DPI), density 72x72, segment length 16, baseline, precision 8, 2999x2249, components 3
```

Nothing special. Then I looked at the hex of the file.

```bash
$ xxd garden.jpg
```

It's outputting many lines, but the interesting part is in the end of the hex. At first glance I didn't realize until I try to use `strings` to extract any readable string inside the file.

```bash
$ strings garden.jpg

... some unreadable strings ...
jc#k
=7g&
mjx/
s\]|."Ue
\qZf
Here is a flag "picoCTF{more_than_m33ts_the_3y3657BaB2C}"
```

And in the end of the output I find the flag **Here is a flag "picoCTF{more_than_m33ts_the_3y3657BaB2C}"**. I realize something was added to the end of the file, and then I rerun `xxd` again and I realize the last bytes there is the flag like this.

```
00230540: eeef 53ae 8620 31b8 751f 9514 f7fb cff5  ..S.. 1.u.......
00230550: a2bb bdac 9687 98e4 d3b2 e87f ffd9 4865  ..............He
00230560: 7265 2069 7320 6120 666c 6167 2022 7069  re is a flag "pi
00230570: 636f 4354 467b 6d6f 7265 5f74 6861 6e5f  coCTF{more_than_
00230580: 6d33 3374 735f 7468 655f 3379 3336 3537  m33ts_the_3y3657
00230590: 4261 4232 437d 220a                      BaB2C}".
```

## Flag

picoCTF{more_than_m33ts_the_3y3657BaB2C}

