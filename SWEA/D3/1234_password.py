##나의 풀이
for test_case in range(1,11):
    n, num = map(int,input().split()) #문자의 총 수 , 문자열
    num_list = list(map(int, str(num)))
    i = 0
    while True:
        if i == len(num_list)-1: #i가 리스트 끝까지 온다면 탈출
            break
        if num_list[i] == num_list[i+1]: #만약 붙어있는 값이 같다면
            num_list.pop(i+1) #뒤에있는 값부터 pop
            num_list.pop(i) #그 다음 앞의 값 pop
            i = 0 #다시 처음부터 본다.
        else:
            i+=1 #붙어있는 값이 같지 않다면 i의 값을 계속 증가시킨다.
    print("#{} {}".format(test_case, int("".join(map(str, num_list)))))

##다른 풀이(stack 이용)
for test_case in range(1, 11):
    n, num = input().split()
    num_list = list(num)
    stack = [] #빈 스택 리스트

    for next_num in num_list: #문자열의 문자를 돌아가보면서 확인한다.
        if next_num not in stack: #만약 아직 스택에 없다면,
            stack.append(next_num) #스택에 문자를 추가한다.
        else: #만약 스택에 있는 숫자라면
            if next_num == stack[-1]: #만약 그 문자가, 스택의 가장 최근에 들어간 문자와 같다면,
                stack.pop() #스택에 들어간 문자를 꺼낸다. 
            else: #만약 문자가 스택의 가장 최근에 들어간 문자와 같지 않다면,
                stack.append(next_num) #그냥 스택에 추가해준다.
    print("#{} {}".format(test_case, "".join(stack)))