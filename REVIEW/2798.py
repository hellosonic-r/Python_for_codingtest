n, m = map(int, input().split())
num_list = list(map(int, input().split()))

num_list.sort()

fin = 0
for i in range(len(num_list)):
    for j in range(i+1, len(num_list)):
        for k in range(j+1,len(num_list)):
            if num_list[i] + num_list[j] + num_list[k] > m:
                continue
            elif num_list[i] + num_list[j] + num_list[k] <= m:
                fin = max(fin, num_list[i] + num_list[j] + num_list[k])

print(fin)

