n = int(input())
m = int(input())
x = [int(xi) for xi in input().split()]
b = [int(bi) for bi in input().split()]


def fun(xj, a):
    ans = 0
    xjj = 1
    for i in range(len(a)):
        ans += (xjj * a[i]) % 23
        xjj = (xjj * xj) % 23
        ans %= 23
    return ans


def convert(ch):
    return chr(ord('a') + ch)


if n == 1:
    for l in range(23):
        ans = True
        for k in range(m):
            bx = fun(x[k], [l])
            if bx != b[k]:
                ans = False
                break
        if ans:
            print(convert(l))
            exit(0)
elif n == 2:
    for l in range(23):
        for r in range(23):
            ans = True
            for k in range(m):
                bx = fun(x[k], [l, r])
                if bx != b[k]:
                    ans = False
                    break
            if ans:
                print(convert(l) + convert(r))
                exit(0)
elif n == 3:
    for j in range(23):
        for l in range(23):
            for r in range(23):
                ans = True
                for k in range(m):
                    bx = fun(x[k], [j, l, r])
                    if bx != b[k]:
                        ans = False
                        break
                if ans:
                    print(convert(j) + convert(l) + convert(r))
                    exit(0)
elif n >= 4:
    for i in range(23):
        for j in range(23):
            for l in range(23):
                for r in range(23):
                    ans = True
                    for k in range(m):
                        bx = fun(x[k], [i, j, l, r])
                        if bx != b[k]:
                            ans = False
                            break
                    if ans:
                        print(convert(i) + convert(j) + convert(l) + convert(r) + 'a' * (n - 4))
                        exit(0)
