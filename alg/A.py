from math import gcd

a, b, c = list(map(int, input().split()))
n = int(input())

if a == b and b == c and a == c:
    print(-1)
    exit(0)

aq = a * b // gcd(a, b)
bq = b * c // gcd(b, c)
cq = a * c // gcd(a, c)

l = 1
r = int(1e18) + 10
while l + 1 < r:
    m = (l + r) // 2
    ans = 0
    ans += m // aq
    ans += m // bq - m // (aq * bq // gcd(aq, bq))
    ans += m // cq - m // (aq * cq // gcd(aq, cq)) - m // (bq * cq // gcd(bq, cq))
    if ans >= n:
        r = m
    else:
        l = m
if r > 1e18:
    print(-1)
else:
    print(r)
