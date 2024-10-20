import sys

s = input()
sum = 0
n = 0
a = {}
while s != "!":
    zn = s[0]
    if zn != '?':
        s = s[2:]
    if zn == '+':
        sid, sai = s.split()
        id = int(sid)
        ai = int(sai.replace(".", ""))
        while id in a:
            pass
        a[id] = ai
        sum += ai
        n += 1
    elif zn == '-':
        id = int(s)
        sum -= a[id]
        del a[id]
        n -= 1
    elif zn == '~':
        sid, sai = s.split()
        id = int(sid)
        ai = int(sai.replace(".", ""))
        sum -= a[id]
        a[id] = ai
        sum += ai
    else:
        # while n == 0:
        #     pass
        print(round(sum / n / 10, 11) if n > 0 else 0, flush=True)

    s = input()
