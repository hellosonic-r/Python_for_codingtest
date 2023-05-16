a, b, v = map(int, input().split())

if ((v-b) / (a-b)) % 1 == 0:
    ans = (v-b) // (a-b)
else:
    ans = ((v-b) // (a-b)) + 1

print(ans)