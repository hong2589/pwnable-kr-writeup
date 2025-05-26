# Run below codes in /tmp/[tmpdir] of pwnable.kr
# Link /home/input2/flag with 'ln -s' to /tmp/[tmpdir]/flag

from pwn import *
import os

# Stage 1
argv = ['' for i in range(100)]
argv[ord('A')] = '\x00'
argv[ord('B')] = '\x20\x0a\x0d'
argv[ord('C')] = '1234'

# Stage 2
r1, w1 = os.pipe()
r2, w2 = os.pipe()
os.write(w1, b'\x00\x0a\x00\xff')
os.write(w2, b'\x00\x0a\x02\xff')

# Stage 3
env = { '\xde\xad\xbe\xef': '\xca\xfe\xba\xbe' }

# Stage 4 
with open('\x0a', 'wb') as f:
    f.write(b'\x00\x00\x00\x00')

p = process(executable='/home/input2/input2', argv=argv, stdin=r1, stderr=r2, env=env)

conn = remote('localhost', 1234)
conn.send(b'\xde\xad\xbe\xef')

p.interactive()
