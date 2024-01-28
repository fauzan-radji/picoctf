# Safe Opener

[Link to the challenge](https://play.picoctf.org/practice/challenge/294)

## Description

Can you open this safe? I forgot the key to my safe but this [program](https://artifacts.picoctf.net/c/83/SafeOpener.java) is supposed to help me with retrieving the lost key. Can you help me unlock my safe? Put the password you recover into the picoCTF flag format like:\
`picoCTF{password}`

## Hints

(None)

## Solution

After I downloaded the file and read the code I found that the password is encrypted by a Base64 algorithm.

```java
public static boolean openSafe(String password) {
    String encodedkey = "cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz";

    if (password.equals(encodedkey)) {
        System.out.println("Sesame open");
        return true;
    }
    else {
        System.out.println("Password is incorrect\n");
        return false;
    }
}
```

So I decode the password and get the flag.

```bash
$ echo "cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz" | base64 -d
pl3as3_l3t_m3_1nt0_th3_saf3
```

Then I just put the flag into the picoCTF flag format.

## Flag

picoCTF{pl3as3_l3t_m3_1nt0_th3_saf3}
