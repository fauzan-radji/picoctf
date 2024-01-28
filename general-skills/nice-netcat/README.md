# Nice netcat...

[Link to the challenge](https://play.picoctf.org/practice/challenge/156)

## Description

There is a nice program that you can talk to by using this command in a shell: `$ nc mercury.picoctf.net 21135`, but it doesn't speak English...

## Hints

- Hint 1: You can practice using netcat with this picoGym problem: [what's a netcat?](https://play.picoctf.org/practice/challenge/34)
- Hint 2: You can practice reading and writing ASCII with this picoGym problem: [Let's Warm Up](https://play.picoctf.org/practice/challenge/22)

## Solution

First, we need to connect to the server using netcat. We can do this by running the following command in a shell:

```bash
$ nc mercury.picoctf.net 21135
112
105
99
111
...
10
```

Then, I use `tee` to write the output to a file called `output.txt`.

```bash
$ nc mercury.picoctf.net 21135 | tee output.txt
```

Then I use this js code to convert to string of flag and named the file as `index.js`.

```javascript
console.log(
  require("fs")
    .readFileSync("./output.txt", "utf8")
    .trim()
    .split(" \n")
    .map((e) => String.fromCharCode(e))
    .join("")
);
```

```bash
$ node index.js
picoCTF{g00d_k1tty!_n1c3_k1tty!_afd5fda4}
```

## Flag

picoCTF{g00d_k1tty!\_n1c3_k1tty!\_afd5fda4}
