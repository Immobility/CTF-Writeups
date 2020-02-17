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
