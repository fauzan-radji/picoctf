# Mind your Ps and Qs

[Link to the challenge](https://play.picoctf.org/practice/challenge/162)

## Description

In RSA, a small `e` value can be problematic, but what about `N`? Can you decrypt this? [values](https://mercury.picoctf.net/static/2604f8b51a5cc62d38a3736938f19cef/values)

## Hints

- Hint 1: Bits are expensive, I used only a little bit over 100 to save money

## Solution

First I downloaded the file and looked at it.

```
Decrypt my super sick RSA:
c: 861270243527190895777142537838333832920579264010533029282104230006461420086153423
n: 1311097532562595991877980619849724606784164430105441327897358800116889057763413423
e: 65537
```

I then used [this website](https://www.dcode.fr/rsa-cipher) to decrypt the message by entering the values into the website.

## Flag

picoCTF{sma11_N_n0_g0od_13686679}
