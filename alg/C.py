s = input()

mas = [0]
for ch in s:
    mas.append(mas[-1] + (-1 if ch == 'L' else 1))
stack = [mas[-1]]
for i in range(len(mas) - 2, -1, -1):
    if stack[-1] <= mas[i]:
        stack.append(mas[i])
k = 0
m = min(mas)
ans = stack[-1] - m
for i in range(len(s)):
    if s[i] == '?':
        k += 2
    m = min(m, mas[i + 1] - k)
    ans = max(ans, (stack[-1] - k) - m)
    if stack[-1] == mas[i + 1]:
        stack.pop()

ans1 = ans

mas = [0]
for ch in s:
    mas.append(mas[-1] + (-1 if ch == 'R' else 1))
stack = [mas[-1]]
for i in range(len(mas) - 2, -1, -1):
    if stack[-1] <= mas[i]:
        stack.append(mas[i])
k = 0
m = min(mas)
ans = stack[-1] - m
for i in range(len(s)):
    if s[i] == '?':
        k += 2
    m = min(m, mas[i + 1] - k)
    ans = max(ans, (stack[-1] - k) - m)
    if stack[-1] == mas[i + 1]:
        stack.pop()

print(max(ans1,ans))
