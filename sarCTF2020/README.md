First public CTF in 2020! 85th place, not bad, A good start to the year!

Note: The flags for this CTF is case-insensitive

# Forensics

Doc. Holmes
-----
```Prompt: Sherlock got it on his super secret channels. You have received a copy of mail. Is everything okay with it?```

Pretty simple, using ```file some.file``` gives us ```Microsoft Word 2007+```, renamed it, then open it up and it gives us a piece of work in a word document with a few random pictures.  After extracting with binwalk, I went to the ```_some.doc.extracted/word/media```, then noticed that the original document had 2 pictures shown, but this contained 3. So opened ```image3.jpg``` then got the flag.
![](https://raw.githubusercontent.com/Immobility/CTF-Writeups/master/sarCTF2020/images/image3.jpg)
```FLAG{prominentplace}```

Blogger
-----
```Recently, John's keys began to be pressed by themselves when he runs his blog. You need to figure out what's the matter.```

USB inputs can be traced with pcap files, the USB HID usage tables can be found on USB.org. The manual can be found [here](https://www.usb.org/sites/default/files/documents/hut1_12v2.pdf) Page 53. I then traced source from 1.7.1 to host because of remote usage, then traced the last few bytes of the inputs. 

Since we're looking for ```FLAG```, I looked for the usage IDs, 09, 0F, 04, 0A, respectively. Which leads to packet 541.
![](https://raw.githubusercontent.com/Immobility/CTF-Writeups/master/sarCTF2020/images/usb1.png) F

![](https://raw.githubusercontent.com/Immobility/CTF-Writeups/master/sarCTF2020/images/usb2.png) L

![](https://raw.githubusercontent.com/Immobility/CTF-Writeups/master/sarCTF2020/images/usb3.png) A

![](https://raw.githubusercontent.com/Immobility/CTF-Writeups/master/sarCTF2020/images/usb4.png) G

Decrypt it up to the ```}``` symbol and you get
```FLAG{like_a_b100dh0und}```

crossw0rd
-----
After disassembling the ELF file, we get
![](https://raw.githubusercontent.com/Immobility/CTF-Writeups/master/sarCTF2020/images/cross1.png)
Get into the ```_Z5checkv``` and we see
![](https://raw.githubusercontent.com/Immobility/CTF-Writeups/master/sarCTF2020/images/cross2.png)
The top part is taking in an input, hence we see the ```_scanf``` function. Let's check the ```_Z1ePc``` function.


Intersting, looks like there is a function inside the function since it calls. Let's try going in the loop and find out.

```Func _Z1ePc```
![](https://github.com/Immobility/CTF-Writeups/blob/master/sarCTF2020/images/cross3.1.png)

```Func _Z1bPc```
![](https://github.com/Immobility/CTF-Writeups/blob/master/sarCTF2020/images/cross3.2.png)

```Func _Z1dPc```
![](https://github.com/Immobility/CTF-Writeups/blob/master/sarCTF2020/images/cross3.3.png)

```Func _Z1fPc```
![](https://github.com/Immobility/CTF-Writeups/blob/master/sarCTF2020/images/cross3.4.png)

```Func _Z1cPc```
![](https://github.com/Immobility/CTF-Writeups/blob/master/sarCTF2020/images/cross3.5.png)

```Func _Z1aPc```
![](https://github.com/Immobility/CTF-Writeups/blob/master/sarCTF2020/images/cross3.6.png)

So we start in *```_Z1ePc```*, let's get the values that we need:

add rax, 7
cmp     al, 35h ; '5'

add rax, 11h
cmp     al, 67h ; 'g'

add rax, 2
cmp     al, 41h ; 'A'

*```_Z1bPc```*

add rax, 0Fh
cmp     al, 69h ; 'i'

add rax, 9
cmp     al, 72h ; 'r'

add rax, 1
cmp     al, 4Ch ; 'L'

*```_Z1dPc```*

add rax, 0Ah
cmp     al, 33h ; '3'

add rax, 12h
cmp     al, 7Dh ; '}'

add rax, 6
cmp     al, 61h ; 'a'

*```_Z1fPc```*

cmp     al, 46h ; 'F'

add rax, 0Eh
cmp     al, 35h ; '5'

add rax, 10h
cmp     al, 6Eh ; 'n'

*```_Z1cPc```*

add rax, 3
cmp     al, 47h ; 'G'

add rax, 0Bh
cmp     al, 76h ; 'v'

add rax, 5
cmp     al, 33h ; '3'

*```_Z1aPc```*

add rax, 4
cmp     al, 7Bh ; '{'

add rax, 0Ch
cmp     al, 33h ; '3'

add rax, 8
cmp     al, 79h ; 'y'

add rax, 0Dh
cmp     al, 72h ; 'r'

Since we loaded our string to rax, think of the string as an array. rax is our array and basically adding to it shows us the position of the array that we're trying to compare the character to. So what do we do? Of course, put the numbers that are getting "added" to rax in order. The highest number we see is 12h, which means there are 19 characters in the strin
g because we need to include the 0th array value. After rearranging them, we get the flag:
```FLAG{3a5yr3v3r5ing}```

Let's check!
![](https://github.com/Immobility/CTF-Writeups/blob/master/sarCTF2020/images/cross4.png)
