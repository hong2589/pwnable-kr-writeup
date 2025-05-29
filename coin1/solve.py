from pwn import *
context.log_level = 'debug'

def binary_search(p, st, en, c):
    while st < en:
        mid = (st+en)//2
        log.success(f"(st, mid, en) = ({st}, {mid}, {en})")

        query = ""
        for k in range(st, mid+1):
            query += str(k) + ' '
        p.sendline(query.encode())
        res = int(p.recvline()[:-1])
        if res % 10 == 0:
            st = mid+1
        else:
            en = mid
        c -= 1
        if c == 0:
            break

    while c >= 1:
        p.sendline(str(st).encode())
        c -= 1
    return st


p = remote('localhost', 9007)
p.recvuntil(b"sec... -")

for i in range(100):
    p.recvuntil(b"N=")
    n = int(p.recvuntil(b" "))
    p.recvuntil(b"C=")
    c = int(p.recvline()[:-1])

    st = 0
    en = n
    ans = binary_search(p, st, en, c)
    p.sendline(str(ans).encode())

p.interactive()
