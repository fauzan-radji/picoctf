# keygenme-py

[Link to the challenge](https://play.picoctf.org/practice/challenge/121)

## Description

[keygenme-trial.py](https://mercury.picoctf.net/static/9055e7d35f5f4646338a1734aea0dda5/keygenme-trial.py)

## Hints

(None)

## Solution

After downloading the file, I take a look inside the script. It's a script that generate a `keygenme.py` file if the key is correct. It has these lines, but the middle part is "dynamic". Apparently, the key is the flag itself.

```python
key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial
```

I need to find the `key_part_dynamic1_trial` part. I found these lines that validate the key.

```python
def check_key(key, username_trial):

    global key_full_template_trial

    if len(key) != len(key_full_template_trial):
        return False
    else:
        # ... some code

        return True
```

First it checks the length of the key.

```python
def check_key(key, username_trial):

    global key_full_template_trial

    if len(key) != len(key_full_template_trial):
        return False
    else:
        # Check static base key part --v
        i = 0
        for c in key_part_static1_trial:
            if key[i] != c:
                return False

            i += 1

        # ... some code

        return True
```

Then it checks the first static part of the key.

```python
def check_key(key, username_trial):

    # ... some code

    else:
        # ... some code

        # TODO : test performance on toolbox container
        # Check dynamic part --v
        if key[i] != hashlib.sha256(username_trial).hexdigest()[4]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[5]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[3]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[6]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[2]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[7]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[1]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[8]:
            return False

        return True
```

It checks the next part of the key by comparing it with some characters of the hash of the username. So I think I can just get the hash then get the characters based on the index. So I come up with this script called `solve.py`.

```python
import hashlib

indexes = [4, 5, 3, 6, 2, 7, 1, 8]

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = ""
key_part_static2_trial = "}"

username_trial = b"FRASER"
key = hashlib.sha256(username_trial).hexdigest()
i = 0
for c in indexes:
    key_part_dynamic1_trial += key[c]
    i += 1

key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial
print(key_full_template_trial)
```

I get the username from the script.

```bash
$ python3 solve.py
picoCTF{1n_7h3_|<3y_of_ac73dc29}
```

After that, I try to validate it using the `keygenme-trial.py` script.

```bash
$ python3 keygenme-trial.py
===============================================
Welcome to the Arcane Calculator, FRASER!

This is the trial version of Arcane Calculator.
The full version may be purchased in person near
the galactic center of the Milky Way galaxy.
Available while supplies last!
=====================================================


___Arcane Calculator___

Menu:
(a) Estimate Astral Projection Mana Burn
(b) [LOCKED] Estimate Astral Slingshot Approach Vector
(c) Enter License Key
(d) Exit Arcane Calculator
What would you like to do, FRASER (a/b/c/d)? c

Enter your license key: picoCTF{1n_7h3_|<3y_of_ac73dc29}

Full version written to 'keygenme.py'.

Exiting trial version...

===================================================

Welcome to the Arcane Calculator, tron!
```

It works! That means the flag is correct.

## Flag

picoCTF{1n*7h3*|<3y_of_ac73dc29}
