p = list(input())
h = 10

for i in range(len(p)-1):
    if p[i] == p[i+1]:
        h += 5
    if p[i] != p[i+1]:
        h += 10

print(h)