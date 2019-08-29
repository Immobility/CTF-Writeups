Patches
-------------

When we first run the code, we get ```Woah there! you jumped over the flag.```

Our original disassembly code looks like 

![](https://github.com/Immobility/CTF-Writeups/blob/master/sunshineCTF-2019/patches/pics/patches1.png)

so what we want to do is to get to one of the other functions that doesn't "Jump over the flag". So we need to refactor one of the addresses assembly function so that the jump instruction goes to either one of the other functions. 

![](https://github.com/Immobility/CTF-Writeups/blob/master/sunshineCTF-2019/patches/pics/patches2.png)

So we're going to change the instruction of ```jnz short loc_5A3``` to ```jz short loc_5A3``` to get the flag ```sun{To0HotToHanDleTo0C0ldToH0ld!}```


![](https://github.com/Immobility/CTF-Writeups/blob/master/sunshineCTF-2019/patches/pics/patches3.png)

