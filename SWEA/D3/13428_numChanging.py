def dfs(count, check_list):
    global max_ans, min_ans
    #한 번 숫자를 교환한다면 리턴
    if count == 1:
        #첫 번째 자리가 0이 아니고, 새로운 최소값이라면
        if check_list[0] != 0 and min_ans > int("".join(map(str, check_list))):
            #최소값 갱신
            min_ans = int("".join(map(str, check_list)))
        #새로운 최대값이라면 최대값 갱신
        if max_ans < int("".join(map(str, check_list))):
            max_ans = int("".join(map(str, check_list)))
        return 
    
    dfs(count+1, check_list) #숫자교환 한번도 안했을 때도 생각해야함

    #숫자 교환 해보기
    for i in range(len(num_list)-1):
        for j in range(i+1, len(num_list)):
            num_list[i], num_list[j] = num_list[j], num_list[i] #숫자 교환
            temp_list = num_list #임시 리스트에 저장
            dfs(count+1, temp_list) #임시 리스트를 파라미터로 해서 호출
            num_list[i], num_list[j] = num_list[j], num_list[i] #다시 숫자 원상복귀

t = int(input())
for test_case in range(1,t+1):
    num = int(input())
    num_list = list(map(int, str(num)))
    min_ans = 1000000000 #최소값 구하기 위한 변수
    max_ans = 0 #최대값 구하기 위한 변수
    if num == 0: #숫자가 0이면 그냥 최소 최대값 0 출력
        print("#{} {} {}".format(test_case, 0, 0))
    else:
        dfs(0,num_list)
        print("#{} {} {}".format(test_case, min_ans, max_ans))