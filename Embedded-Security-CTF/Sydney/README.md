Oof, took a while to upload new stuffs after procrastinating for a bit, but here it is!

The portion of the main function that we want to see:

![](https://github.com/Immobility/CTF-Writeups/blob/master/Embedded-Security-CTF/Sydney/t3.1.png)

The check_password function is as shown:

![](https://github.com/Immobility/CTF-Writeups/blob/master/Embedded-Security-CTF/Sydney/t3.2.png)

So basically we can see that the answer is basically like the New Orleans one, we can convert from hex to ascii and get the answer as ```1Biyl^^e```!

But is it? Because once we insert our letters, we get an invalid password, so that's wrong. So lets check the memory.

![](https://github.com/Immobility/CTF-Writeups/blob/master/Embedded-Security-CTF/Sydney/t3.3.png)

After analyzing the input, we come to a conclusion that the input is, in fact, not checked as big endian, but as little endian, so we must reverse every 2 bytes of our input.  


Our answer: ```B1yi^le^```
