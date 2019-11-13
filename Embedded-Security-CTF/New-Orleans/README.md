This one somewhat feels much easier than the tutorial. In the main function, we see a function called ```create_password```, hmm I wonder what that could mean?

![](https://raw.githubusercontent.com/Immobility/CTF-Writeups/master/Embedded-Security-CTF/New-Orleans/t2.1.png)

I took a look at the function and found

![](https://raw.githubusercontent.com/Immobility/CTF-Writeups/master/Embedded-Security-CTF/New-Orleans/t2.2.png)

```
447e <create_password>
447e:  3f40 0024      mov	#0x2400, r15
4482:  ff40 2800 0000 mov.b	#0x28, 0x0(r15) 
4488:  ff40 2d00 0100 mov.b	#0x2d, 0x1(r15)
448e:  ff40 4700 0200 mov.b	#0x47, 0x2(r15)
4494:  ff40 5600 0300 mov.b	#0x56, 0x3(r15)
449a:  ff40 5200 0400 mov.b	#0x52, 0x4(r15)
44a0:  ff40 2d00 0500 mov.b	#0x2d, 0x5(r15)
44a6:  ff40 6f00 0600 mov.b	#0x6f, 0x6(r15)
44ac:  cf43 0700      mov.b	#0x0, 0x7(r15)
44b0:  3041           ret
```

Interesting! Let's convert the hex to ascii: ```(-GVR-o```

Could this be our password?

The ```check_password``` function compares each letter in 0x2400 byte by byte to the value at r13, so that is our solution!

![](https://raw.githubusercontent.com/Immobility/CTF-Writeups/master/Embedded-Security-CTF/New-Orleans/t2.3.png)
