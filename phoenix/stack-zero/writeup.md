# So why does this solution work?

First let's understand how stacks work.
When we take a look at the source code, we see that 
"char buffer[64]" and "volatile int changeme" are declared.
In assembly, when these variables are called, they're loaded into what's called a stack.

One important thing to understand is that stack grows downward in order when the eip tells the machine to declare a variable or call a function. In this case, "char buffer[64]" is called first. So the first 8 bytes (x86 machine) of the stack of which the variables are called would look like this:

![](https://github.com/Immobility/CTF-Writeups/blob/master/phoenix/stack-zero/image1.png?raw=true)

Let's check on gdb. Right from the stack, although we should already know how big the buffer space of "char buffer" should be, but we can roughly get the space by putting a breakpoint right after the input is called and insert a test input. ```(b *0x080484e9)```

![](https://github.com/Immobility/CTF-Writeups/blob/master/phoenix/stack-zero/image2.png?raw=true)

![](https://github.com/Immobility/CTF-Writeups/blob/master/phoenix/stack-zero/image3.png?raw=true)

Right when we get to our breakpoint, lets open $esp and search for the input. In this example, we'll search for 80 bytes. ```x/80x $esp```

![](https://github.com/Immobility/CTF-Writeups/blob/master/phoenix/stack-zero/image4.png?raw=true)

Our "A"s are from 0xffffd0ec and onwards. So that means we can probably find the value of this buffer manually depending how many bytes that contain nothing exists. Continue stepping over (or press ```c``` ) and we'll get an output of 

```"Uh oh, 'changeme' has not yet been changed. Would you like to try again?"```

This time, lets try inputting more "A"s, this time 65, and we'll get the output of 

```"Well done, the 'changeme' variable has been changed!"```

However, when we take a look at $esp, we see that the one byte at 0xffffd12c made a difference in the output. 

# So why?

When we take a look back at the assembly, we can see that we're trying to compare something that's in the eax function by moving whatever is in the value of [ebp-0xc] to eax.

![](https://github.com/Immobility/CTF-Writeups/blob/master/phoenix/stack-zero/image6.png?raw=true)

We can determined what [ebp-0xc] is by typing ```p *(int *)($ebp-0xc)```. If the number of "A" were lower than the amount of buffers it took to fill char buffer[64], then the value of ($ebp-0xc) wouldn't have changed at all. However, once we fill enough buffers to overflow it on to the stack, we can observe that the value of ($ebp-0xc) changed to 0x41. Thus, replacing the original value of what was supposed to be "changeme = 0" to "changeme = 0x41"

![](https://github.com/Immobility/CTF-Writeups/blob/master/phoenix/stack-zero/image7.png?raw=true)
