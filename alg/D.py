N = 1
print(N)
ans = input()
if ans == "ok":
    print(f"! {N}")
    exit(0)
while True:
    wop = N * 2
    print(wop)
    ans = input()
    while ans == "fail":
        pass
    if ans == "wet":
        N *= 2
    else:
        break

l = N
r = N * 2

while l + 1 < r:
    m = (l + r) // 2
    print(m)
    ans = input()
    while ans == "fail":
        pass
    if ans == "wet":
        l = m
    else:
        r = m
print(f"! {r}")
