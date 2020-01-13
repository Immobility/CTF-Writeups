This one is a simple buffer overflow program. At first, in the main, we only see the login function and a clear r15.
![](https://github.com/Immobility/CTF-Writeups/blob/master/Embedded-Security-CTF/Hanoi/t4.1.png)

By analyzing the login function, we see the login function.

![](https://github.com/Immobility/CTF-Writeups/blob/master/Embedded-Security-CTF/Hanoi/t4.2.png)

So what's wrong with this? The program first uses the ```gets``` function (labeled as getsn) and since this is basically around the 4th challenge, the password reminds us that the password should between 8 and 16 characters. The most interesting thing we see is 

![](https://github.com/Immobility/CTF-Writeups/blob/master/Embedded-Security-CTF/Hanoi/t4.3.png)

In address 4540, our input is stored there, however, in address 454c, we move a byte to 0x2410. That means, the byte at 2411 must be moved. Since address 455a compares byte between whatever's in 0x2410 and an instant 0xa2, we can exploit the input.

By checking the hex encoded input and first filling the first 16 byte buffers with A's (20 in hex), we get the solution 
```20202020202020202020202020202020a2```!

![](https://github.com/Immobility/CTF-Writeups/blob/master/Embedded-Security-CTF/Hanoi/t4.4.png)

![](https://github.com/Immobility/CTF-Writeups/blob/master/Embedded-Security-CTF/Hanoi/t4.5.png)
