n, k = map(int, input().split()) 
coin_types = []
for i in range(n):
    coin_types.append(int(input()))

coin_types.sort(reverse = True)
#[50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1]
count = 0
for j in range(n): # k = 4200 일때
    if k // coin_types[j] >= 1:
        count = count + k // coin_types[j]
        k = k % coin_types[j]
    else:
        continue

print(count)