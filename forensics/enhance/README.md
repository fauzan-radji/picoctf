# Enhance!

## Description

Download this image file and find the flag.

- [Download image file](https://artifacts.picoctf.net/c/102/drawing.flag.svg)

## Hints

(None)

## Solution

First I open the svg normally and seeing only a black circle with white smaller inner circle. I suspect there is some text hidden inside this svg file so I `cat` the content of the file, I'm looking for `<text></text>` tag.

```bash
$ cat drawing.flag.svg

... some svg tags ...
    <text
       xml:space="preserve"
       style="font-style:normal;font-weight:normal;font-size:0.00352781px;line-height:1.25;font-family:sans-serif;letter-spacing:0px;word-spacing:0px;fill:#ffffff;fill-opacity:1;stroke:none;stroke-width:0.26458332;"
       x="107.43014"
       y="132.08501"
       id="text3723"><tspan
         sodipodi:role="line"
         x="107.43014"
         y="132.08501"
         style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
         id="tspan3748">p </tspan><tspan
         sodipodi:role="line"
         x="107.43014"
         y="132.08942"
         style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
         id="tspan3754">i </tspan><tspan
         sodipodi:role="line"
         x="107.43014"
         y="132.09383"
         style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
         id="tspan3756">c </tspan><tspan
         sodipodi:role="line"
         x="107.43014"
         y="132.09824"
         style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
         id="tspan3758">o </tspan><tspan
         sodipodi:role="line"
         x="107.43014"
         y="132.10265"
         style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
         id="tspan3760">C </tspan><tspan
         sodipodi:role="line"
         x="107.43014"
         y="132.10706"
         style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
         id="tspan3762">T </tspan><tspan
         sodipodi:role="line"
         x="107.43014"
         y="132.11147"
         style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
         id="tspan3764">F { 3 n h 4 n </tspan><tspan
         sodipodi:role="line"
         x="107.43014"
         y="132.11588"
         style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
         id="tspan3752">c 3 d _ d 0 a 7 5 7 b f }</tspan></text>
```

Actually from here I can see the flag already, but I wan't to change the text color instead. I want to edit the color `#ffffff` to something else and I use vscode to change all the ocurences at the same time. After that I tried to open the file, still no text appear. I inspect the code one more time carefully and I realize there is a `style` attribute in the `<text></text>` tag that made the text disappear.

```
style="font-style:normal;font-weight:normal;font-size:0.00352781px;line-height:1.25;font-family:sans-serif;letter-spacing:0px;word-spacing:0px;fill:#ffffff;fill-opacity:1;stroke:none;stroke-width:0.26458332;"
```

Actually I can change them manually but at this point I just decided to assemble the flag by hand.

## Flag

picoCTF{3nh4nc3d_d0a757bf}
