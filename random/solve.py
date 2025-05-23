from pwn import *

context.log_level = 'debug'

ssh_conn = ssh(host='pwnable.kr', port=2222, user='random', password='guest')
p = ssh_conn.process('random')

random = 0x6b8b4567
target = 0xcafebabe
key = target ^ random

p.sendline(str(key).encode())
p.interactive()
