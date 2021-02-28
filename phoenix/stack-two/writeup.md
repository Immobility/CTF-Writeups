# Writeup

This solution is very similar to stack-one except this time, you need to declare an environmental variable. This can be done by implementing "os" module and setting it equal to the buffer and the jump address.

"os.environ["ExploitEducation"]" sets the environmental variable called "ExploitEducation" on to the local environment. We could now set the buffer string that we wrote and set it so that "ExploitEducation" holds the value of 64 "A"s and the address of the address of the win function, "0x0d0a090a".
