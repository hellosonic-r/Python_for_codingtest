
dwarfs_list = []
s = 0
for i in range(9):
    n = int(input())
    dwarfs_list.append(n)

sorted_dwarfs_list = sorted(dwarfs_list)

s = sum(sorted_dwarfs_list) - 100

incorrect_dwarfs_index = []
for j in range(9):
    for k in range(9):
        if j == k:
            continue
        elif sorted_dwarfs_list[j] + sorted_dwarfs_list[k] == 40:
            incorrect_dwarfs_index = [j,k]
            break
    if incorrect_dwarfs_index:
        break

sorted_dwarfs_list.pop(incorrect_dwarfs_index[0])
sorted_dwarfs_list.pop(incorrect_dwarfs_index[0])
for z in range(7):
    print(sorted_dwarfs_list[z])


#실행되는데 런타임에러...