Upon opening the file, we start out with... this interesting image:

![](https://raw.githubusercontent.com/Immobility/CTF/master/tamuctf-2019/images/art.png)

Upon using the ```strings``` command, we get some gibberish with a base64 encrypted text: 
```
TmljZSB0cnksIGJ1dCB0aGVyZSBpcyBubyBmbGFnIGhlcmUuCllvdSBzaG91bGQgY2hlY2sgdGhp
cyBtdXNpYyB2aWRlbyBvdXQgdGhvdWdoLCBpdCdzIHByZXR0eSBjb29sLgpodHRwczovL3d3dy55
b3V0dWJlLmNvbS93YXRjaD92PVR1SnFVdkJqNHJFCg==
```

and some other files, however upon decoding the file, it gives us a red herring:
```
Nice try, but there is no flag here.
You should check this music video out though, it's pretty cool.
https://www.youtube.com/watch?v=TuJqUvBj4rE
```

Although pretty disappointed, after looking/skimming through the string output, we can see there are actually more files inside the picture like:
```
not_the_flag.txtUT	
Sorry, no flag here
_rels/.relsPK
docProps/app.xmlPK
docProps/core.xmlPK
word/_rels/document.xml.relsPK
word/settings.xmlPK
word/fontTable.xmlPK
word/media/image1.pngUT
word/document.xmlPK
word/styles.xmlPK
[Content_Types].xmlPK
not_the_flag.txtUT
```

This prompted me to think that there are actually more files hidden underneath, and used ```binwalk``` to open up the file, then skimmed through the files and found an interesting image of the popular meme of "Not sure if.." of Fry from Fururama. I ```strings```'d that output and we see a ```ZmxhZ3tQMGxZdEByX0QwX3kwdV9HM3RfSXRfTjB3P30K``` in the end. Which also is decoded to:

```
flag{P0lYt@r_D0_y0u_G3t_It_N0w?}
```
