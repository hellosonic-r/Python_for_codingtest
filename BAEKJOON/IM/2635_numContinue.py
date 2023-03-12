n = int(input())

fin = 0 #개수
fin_num = [] #그 숫자 
for i in range(1,n+1):
    num_list = []
    num_list.append(n)
    num_list.append(i)
    num_list.append(n-i)
    j = 3
    while True: 
        value = num_list[j-2] - num_list[j-1] 
        if value < 0:
            break
        else:
            j += 1
            num_list.append(value)
    if j >= fin:
        fin = j
        fin_num = num_list
    else:
        continue

print(fin)
for i in range(len(fin_num)):
    print(fin_num[i],end = " ")
    if i ==len(fin_num) - 1:
        print()