t = int(input())
for i in range(t):
    n = int(input())
    mas = list(map(int, input().split()))
    ans = 0
    try:
        i = 0
        while i < n:
            l, r = i, i + 1
            if mas[l] >= mas[r]:
                i = r
                continue
            while mas[r] < mas[r + 1]:
                r += 1
            if mas[r] == mas[r + 1]:
                i = r
                continue
            maxim_id = r
            while r + 1 < n and mas[r] > mas[r + 1]:
                r += 1
            ans += (maxim_id - l) * (r - maxim_id)
            i = maxim_id + 1
    except:
        pass
    print(ans)
