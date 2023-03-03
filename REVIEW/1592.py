n,m,l = map(int, input().split())

count_list = [1] + ([0]*(n-1)) 

count = 0
i = 0
while True:
    if m in count_list:
        break
    if count_list[i] % 2 != 0:
        count_list[(i+l)%n] += 1 
        count += 1
        i = (i+l)%n
    else:
        count_list[-((l-i)%n)] += 1
        count += 1
        i = -((l-i)%n)

print(count)