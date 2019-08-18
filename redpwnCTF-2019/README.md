BabbyPwn
------------------------
```
Written by: blevy

nc chall2.2019.redpwn.net 4001
```

Since the chalenge is an introductory overflow challenge, the most basic type of pwn is buffer overflow, therefore spamming letters in the console will automatically update the printout and print out the flag.

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

We can decode this by writing ```eval(f=>atob([...atob(f)].map(s=>String.fromCharCode(s.charCodeAt(0)-(location.host.charCodeAt(0)%location.host.charCodeAt(3)))).join('')))('vdDby72W15O2qrnJtqep0cSnsd3HqZzbx7io27C7tZi7lanYx6jPyb2nsczHuMec')```

which gives us
```"flag{tHe_H1gh3st_quA11ty_antI_d3buG}"```

Generic Crack Me
------------
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
