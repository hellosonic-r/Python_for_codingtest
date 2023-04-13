n, k = map(int,input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))

coin.sort(reverse=True)


for i in range(n):
    coin[i]