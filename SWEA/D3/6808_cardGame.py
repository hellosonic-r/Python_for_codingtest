def dfs(count,gy,iy):
    global gy_win, gy_lose
    if count == 9: #9개를 다 뽑았다면,
        #규영의 총점과 인영의 총점을 비교
        if gy>iy: 
            gy_win += 1
        if gy<iy:
            gy_lose += 1
        return
    for i in range(len(iy_list)):
        if v[i] == 0: #중복하여 카드를 뽑는 것을 막기위한 방문처리
            v[i] = 1
            #규영이가 뽑은 0~8번 인덱스의 카드와 인영이가 무작위로 뽑은 카드를 비교 
            if gy_list[count] > iy_list[i]:
                next_gy = gy+gy_list[count]+iy_list[i]
                next_iy = iy
            elif gy_list[count] < iy_list[i]:
                next_gy = gy
                next_iy = iy+gy_list[count]+iy_list[i]
            dfs(count+1, next_gy, next_iy)
            v[i] = 0

t = int(input())
for test_case in range(1,t+1):
    gy_list = list(map(int, input().split()))
    iy_list = []
    for i in range(1,19):
        if i not in gy_list:
            iy_list.append(i)
    v = [0] * 9
    gy_win = 0
    gy_lose = 0
    dfs(0,0,0)
    print("#{} {} {}".format(test_case, gy_win, gy_lose))
