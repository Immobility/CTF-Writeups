# Writeup

When we first disassemble our code, we see the "gets" function. We can also see the complete\_level function.

In the source code, we can also see that there are 64 bytes of buffers in the "buffer" variable as well a "volatile int (*fp)" **POINTER**. This is a big flag as we can use the pointer declaration to redirect it onto an uncalled function, hence the "complete_level" function.

So the address of the "complete_level" function is 0x08048535. Using this info, we can create the string of 64 "A"s followed by \x35\x85\x04\x08 (little endian of complete_level).
