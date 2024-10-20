n, h = map(int, input().split())
ls = list(map(int, input().split()))
dr = {}
mas = set()
for i in range(n):
    for j in range(ls[i]):
        ss = input()
        s = int(ss[0])
        if s == 0:
            continue
        ss = [int(x) for x in ss[2:].split()]
        for z in ss:
            if z not in dr:
                dr[z] = []
            dr[z].append((i + 1, j + 1))
            mas.add(z)
ansx = 0
ansy = 0
mas = list(mas)
mas.sort()
for key in mas:
    for i in range(0, len(dr[key]), h):
        ans = dr[key][i:min(i + h, len(dr[key]))]
        for an in ans:
            print(f"1 {an[0]} {an[1]} 0")
        print(3)
        ansx += 1
    ansy += (len(dr[key]) - 1) // h + 1

print(0)
