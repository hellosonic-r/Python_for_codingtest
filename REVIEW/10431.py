t = int(input())
for test_case in range(1,t+1):
    num_list = list(map(int, input().split()))
    num_list.pop(0)
    cnt = 0
    for i in range(len(num_list)-1, 0, -1): #맨 뒤에 픽
        for j in range(i-1, -1,-1): #그 앞에 픽
            if num_list[i] < num_list[j]:
                num_list[i], num_list[j] = num_list[j], num_list[i]
                cnt += 1
                
    print(test_case, cnt)
