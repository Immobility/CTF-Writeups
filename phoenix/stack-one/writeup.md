# Writeup

From stack-zero, we understood that certain values in the stack can be manipulated. From here, we can use this information to change the value of "changeme" next to the "buffer" to the value of "0x496c5962".

So we would require 64 bytes to fill the initial buffer and to end it with the byte string of "0x496c5962". The program was designed in little endian, so we would need to revert the byte string from "\x49 \x6c \x59 \x62" to "\x62 \x59 \x6c \x49" for out input.

So to create our input in Python 3, our input should be ```"A" * 64 + '\x62\x59\x6c\x49'```
