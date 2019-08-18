BabbyPwn
------------------------
```
Written by: blevy

nc chall2.2019.redpwn.net 4001
```

Since the chalenge is an introductory overflow challenge, the most basic type of pwn is buffer overflow, therefore spamming letters such as "aaaaaaaaaaaaaaaaaa" in the console will automatically update the printout and print out the flag.

Crypt
------------------
```
Written by: ginkoid

Store your most valuable secrets with this new encryption algorithm.
```

Right as we get in the page, we see
```Your safely encrypted flag is vdDby72W15O2qrnJtqep0cSnsd3HqZzbx7io27C7tZi7lanYx6jPyb2nsczHuMec```

By going to Inspector and checking the code, the algorithm is enclosed by JSFuck, which gives us
```
f=>btoa([...btoa(f)].map(s=>String.fromCharCode(s.charCodeAt(0)+(location.host.charCodeAt(0)%location.host.charCodeAt(3)))).join(''))
```

We can reverse this encryption by writing ```eval(f=>atob([...atob(f)].map(s=>String.fromCharCode(s.charCodeAt(0)-(location.host.charCodeAt(0)%location.host.charCodeAt(3)))).join('')))('vdDby72W15O2qrnJtqep0cSnsd3HqZzbx7io27C7tZi7lanYx6jPyb2nsczHuMec')```

which gives us
```flag{tHe_H1gh3st_quA11ty_antI_d3buG}```

Generic Crackme
------------
```
Written by: blevy

Note: Enclose the flag with flag{}.
```

Right as we launch IDA, we get into 

![](https://github.com/Immobility/CTF-Writeups/blob/master/redpwnCTF-2019/photos/gcm1.png)

The part we care is the parts right after the \_fgets function where the inputs matter. We will be looking at what the sub_1168 function does.

![](https://github.com/Immobility/CTF-Writeups/blob/master/redpwnCTF-2019/photos/gcm2.png)

A closer pic of the first 2 of the conditions:

![](https://github.com/Immobility/CTF-Writeups/blob/master/redpwnCTF-2019/photos/gcm3closerpic.png)

It seems that theres a sub_1159 function right before the cmp instruction was used.

![](https://github.com/Immobility/CTF-Writeups/blob/master/redpwnCTF-2019/photos/gcm4.png)

After analysing what sub_1159 does, we can conclude that it adds 1 byte to whatever the input was. And since each cmp instruction is comparing each letter by letter in ```rax``` (which is our input), we can assume this works as a caesar cipher and rotate 1 from our input to get ```ephhz```, which our input should be ```doggy```, so our flag should be 

```flag{doggy}```.

Generic Crackme Redux
---------------
```
Written by: blevy

Note: Enclose the flag with flag{}.
```

This part is generic math (haha). By opening IDA, we see

![](https://github.com/Immobility/CTF-Writeups/blob/master/redpwnCTF-2019/photos/gcmr1.png)

Which shows us the disassembly for the main function. We get straight into the sub_5645DEB32169 function, where we see

![](https://github.com/Immobility/CTF-Writeups/blob/master/redpwnCTF-2019/photos/gcmr2.png)

We have to compare our output 0AC292h, which is 705170 in decimal. So lets break the function down. From the start, 

```Lets call edx as x.
mov eax, edx means x = x, so both eax and edx have values of x.
shl eax, 2 means shift eax bits by 2, psudo-meaning multiply eax by 4. So eax = 4x.
add eax, edx means add edx to eax. So eax = 5x
add eax, eax means add eax to eax, or eax * 2. eax =  10x
cmp eax, 0AC292h compares value of eax to 0AC292h
```
Now after static analysizing these sets of functions manually, after we calculate eax, we get a decimal value of 70517, which is the correct answer!

![](https://github.com/Immobility/CTF-Writeups/blob/master/redpwnCTF-2019/photos/gcmr3.png)

So our correct answer is ```flag{70517}```

MSB
---------
```
Written by: NotDeGhost

It's not LSB, its MSB!

Red is Random, Green is Garbage, Blue is Boring.

Hint: Only one channel is correct. Also, I like doing things top down.
```

The challenge gives us a picture and gives some hints that data is hidden by MSB. This gives us the chance to use ```stegsolve```. When opening the picture with stegsolve, we get a picture.

![](https://github.com/Immobility/CTF-Writeups/blob/master/redpwnCTF-2019/photos/msb1.png)

By going through the color planes, we see an output that doesnt really feel the same like the others, there I data extracted by column and got the flag!

![](https://github.com/Immobility/CTF-Writeups/blob/master/redpwnCTF-2019/photos/msb2.png)

![](https://github.com/Immobility/CTF-Writeups/blob/master/redpwnCTF-2019/photos/msb3.png)

```flag{MSB_really_sucks}```
