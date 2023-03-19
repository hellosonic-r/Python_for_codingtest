t = int(input())

for test_case in range(1, t+1):
    #숫자 입력
    num = int(input())
    #입력한 숫자를 리스트로 저장
    num_list = list(map(int, str(num))) 
    #입력한 숫자의 배수를 입력한 숫자에서 빼주면서 비교할 것이므로, 비교할 사본 리스트 생성
    copy_num_list = num_list 
    ans = 0
    #2부터 입력한 숫자 자릿수 중 최대값까지 곱해봄
    for i in range(2, max(num_list)+1): 
        #입력한 숫자의 배수 (x2부터 시작)
        temp_num = num * i
        temp_num_list = list(map(int, str(temp_num))) #285714
        #만약 입력한 숫자의 배수가 입력한 숫자의 자릿수와 달라지면 넘어간다.
        if len(temp_num_list) != len(copy_num_list):
            continue
        #숫자의 배수의 자릿수 
        cnt = len(temp_num_list)
        #숫자의 배수의 자릿수를 하나씩 비교해보는 for문 작성
        for j in range(len(temp_num_list)):
            #만약, 숫자의 배수의 자릿수가, 기존 입력한 숫자에 있는 숫자라면
            if temp_num_list[j] in copy_num_list:
            #cnt를 하나 빼준다.
                cnt -= 1
            #기존 입력한 숫자에 없는 숫자라면
            else:
            #넘어간다.
                continue
        #cnt = 0 즉, 숫자의 배수의 자릿수의 숫자가 기존 입력한 숫자에 다 있다면
        if cnt == 0:
            #ans에 1을 저장한다.
            ans = 1
            #그리고 반복문(배수를 하나하나 살펴보는 반복문)을 탈출한다.(뒤에거는 볼 필요도 없기 때문에)
            break
        #그렇지 않다면 계속해서 반복문을 수행한다.
        else:
            continue
            
    #만약 ans에 1이 저장되어 있다면,
    if ans == 1:
        print("#{} {}".format(test_case, "possible"))
    #가능한 모든 배수를 살펴보았는데도 ans에 1이 저장되지 않았다면,
    else:
        print("#{} {}".format(test_case, "impossible"))
            
                
            