arr = []
for _ in range(9):
    arr.append(int(input()))

fake_sum = sum(arr) - 100

for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        if arr[i] + arr[j] == fake_sum:
            idx_2 = j
            idx_1 = i
            break

arr.pop(idx_2)
arr.pop(idx_1)

arr.sort()

for i in range(len(arr)):
    print(arr[i])
