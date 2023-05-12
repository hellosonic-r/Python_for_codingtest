n = int(input())

num_list = [n]

length = 0
max_length = 0
ans = []
for i in range(1,n+1):
    num_list.append(i) #[n,i] -> [100,1]
    j = 0 
    while True:
        next_num = num_list[j] - num_list[j+1]
        if next_num >= 0:
            num_list.append(next_num)
            j += 1
        else:
            length = len(num_list)
            if max_length < length:
                max_length = length
                ans = num_list
            num_list = [n]
            break

print(max_length)
print(" ".join(map(str, ans)))