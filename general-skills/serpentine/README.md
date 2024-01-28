# Serpentine

[Link to the challenge](https://play.picoctf.org/practice/challenge/251)

## Description

Find the flag in the Python script! [Download Python script](https://artifacts.picoctf.net/c/36/serpentine.py)

## Hints

- Hint 1: Try running the script and see what happens
- Hint 2: In the webshell, try examining the script with a text editor like `nano`
- Hint 3: To exit `nano`, press Ctrl and x and follow the on-screen prompts.
- Hint 4: The `str_xor` function does not need to be reverse engineered for this challenge.

## Solution

After I downloaded the file, I ran it with `python3 serpentine.py` and got the following output:

```
  .-^-.
 /     \      .- ~ ~ -.
()     ()    /   _ _   `.                     _ _ _
 \_   _/    /  /     \   \                . ~  _ _  ~ .
   | |     /  /       \   \             .' .~       ~-. `.
   | |    /  /         )   )           /  /             `.`.
   \ \_ _/  /         /   /           /  /                `'
    \_ _ _.'         /   /           (  (
                    /   /             \  \
                   /   /               \  \
                  /   /                 )  )
                 (   (                 /  /
                  `.  `.             .'  /
                    `.   ~ - - - - ~   .'
                       ~ . _ _ _ _ . ~

Welcome to the serpentine encourager!


a) Print encouragement
b) Print flag
c) Quit

What would you like to do? (a/b/c)
```

I tried to print the flag, but it said:

```
Oops! I must have misplaced the print_flag function! Check my source code!
```

So I opened the file with vscode and found the `main` function does not call the `print_flag` function. I added the following line to the `main` function:

```python
  elif choice == 'b':
      print_flag()
```

Then I ran the script again and got the flag.

## Flag

picoCTF{7h3_r04d_l355_7r4v3l3d_aa2340b2}
