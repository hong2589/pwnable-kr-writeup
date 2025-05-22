from pwn import *

# context.log_level = 'debug'

# Make arg
passcode = 0x21dd09ec
value = passcode // 5
last = passcode - value * 4
arg = p32(value) * 4 + p32(last)

ssh_conn = ssh(host='pwnable.kr', port=2222, user='col', password='guest')
p = ssh_conn.process(executable='col', argv=['col', arg])

p.interactive()
