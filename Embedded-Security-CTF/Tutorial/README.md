After the ```puts function``` in process 4440, the process moves on to the ```get_password``` and the ```check_password``` functions, we're interested in the ```check_password``` function. 
![](https://raw.githubusercontent.com/Immobility/CTF-Writeups/master/Embedded-Security-CTF/Tutorial/t1.1.png)


To do this, we analyze the ```check_password``` function and see

![](https://raw.githubusercontent.com/Immobility/CTF-Writeups/master/Embedded-Security-CTF/Tutorial/t1.2.png)

```
mov.b @r15, r14 <--- saves r14 register byte value to r15
inc r15 <--- increments value of r15
inc r12 <--- increments r12 (Original value is 0 in the register)
test r14 <--- resets CF & ZF to 0
jnz	#0x4484 <check_password+0x0> <--- Repeats moving pointer back to beginning of the check_password loop until zero flag is 1
cmp	#0x9, r12 <--- compares r12 with immediate, 9.
jeq	#0x4498 <check_password+0x14> <--- jumps 20 bytes ahead if equal.
```

So in the end, the input just requires 8 bytes because the r12 increments before the length is checked.

So any value of password should work, such as, "aaaaaaaa" or "testtest" or "!@!@!@!@".

And the door opens!

![](https://raw.githubusercontent.com/Immobility/CTF-Writeups/master/Embedded-Security-CTF/Tutorial/t1.3.png)
