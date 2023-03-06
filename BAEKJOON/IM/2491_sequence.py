###수열

n = int(input())

sequence = list(map(int, input().split()))


big_count = 1
count_list = []
for i in range(len(sequence)):
    if i == 0:
        continue
    elif sequence[i] >= sequence[i-1]:
        big_count += 1
    elif sequence[i] < sequence[i-1]:
        count_list.append(big_count)
        big_count = 1   
count_list.append(big_count)


small_count = 1
for j in range(len(sequence)):
    if j == 0:
        continue
    elif sequence[j] <= sequence[j-1]:
        small_count += 1
    elif sequence[j] > sequence[j-1]:
        count_list.append(small_count)
        small_count = 1
count_list.append(small_count)

print(max(count_list))
