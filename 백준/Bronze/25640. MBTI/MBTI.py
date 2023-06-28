s = input()
n = int(input())

ans = 0

for i in range(n):
    string = input()
    if string == s:
        ans += 1

print(ans)


