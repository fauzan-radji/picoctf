# First Grep

[Link to the challenge](https://play.picoctf.org/practice/challenge/85)

## Description

Can you find the flag in [file](https://jupiter.challenges.picoctf.org/static/495d43ee4a2b9f345a4307d053b4d88d/file)? This would be really tedious to look through manually, something tells me there is a better way.

## Hints

- Hint 1: grep [tutorial](https://ryanstutorials.net/linuxtutorial/grep.php)

## Solution

First I download the file using `wget`.

```bash
$ wget https://ryanstutorials.net/linuxtutorial/grep.php
```

After the file successfully downloaded, then I try to look at the content of the file using `cat`. Here's what I found:

```
yQE:Z:y?9U@Z	Pl6lA%KO0TGr@9#mc`O;zWQePqFFyrZ+dzqMx`I*33T_gNm7[P|_)y8P9=EM8kn$4r/9M$~mG,UD=p2L /-$$mAdfN+:1YGP(A5&!,ry 6 i^0mA*xKVJ`s[3R]a5!r3wlgT>hR$7@V1BLg[MH^	q		,fH>*ib~bkV`E+74%pCB6%DP~#J[QU]qnrSFg?%<!T*ZJGoK>w8^n*|QwcyX;~W9hHmYEj514ECw	rMj84c[;plncW+Zus	PN,3DJJ	!U=9W,e8:Ia BdkN0S+N:.t(fB@O.YWT3[u(Qo4UCy6xS2L,4$Yg-1J-TQ-%~_Ot$QV=~x Z*jPA#kSmkU,jFrXpPAb_wS:P)#zzi),P,i(lKj~ZtlAeM0Ze0/hMQUK*#SxGU5wb9DE)[~N^0+C>u_;j5l~aP1mGg@:V65:|8[32i_$Ee tU1lX.dYt!Ie,5bGlW.T7:KPr!@UY^!jPT6!f)-94?sH2(a$L0pz|l(riTaXBN&IfV;vyh[4&BV2S`^_+~HA-Pcx CjdNY>X2rj>7Jvpgf:[G >Hj&w&Hn>qX`e#I,9j]%6h<nhD$q=aAJlz~ eNaHgX-k*|V	wqAvj& jd7DjJ|Dr7R7f9_5		#o~301nhlwA%,Rcn?hh6](?~u@4V@*
...
```

The content is too long, but we can use `grep` to filter the string.

```bash
$ grep "picoCTF" file
```

Then I found the flag.

## Flag

picoCTF{grep_is_good_to_find_things_dba08a45}
