#for문 이용

arr = []
for _ in range(9):
    arr.append(int(input()))

arr.sort()

s = sum(arr)
incorrect_arr_index = []
for i in range(9):
    for j in range(i+1 , 9):
         if s - arr[i] - arr[j] == 100:
             incorrect_arr_index.append(i)
             incorrect_arr_index.append(j)
incorrect_Dwarf1 = arr[int(incorrect_arr_index[0])]
incorrect_Dwarf2 = arr[int(incorrect_arr_index[1])]

arr.remove(incorrect_Dwarf1)
arr.remove(incorrect_Dwarf2)

for z in range(7):
    print(arr[z])
