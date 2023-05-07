t = int(input())
for test_case in range(1,t+1):
    n = int(input())
    if n % 2 == 0: #짝수 개의 카드일 때,
        length = n//2 
    else: #홀수 개의 카드일 때
        length = (n//2) +1
    string = list(input().split())
    stack = []
    #반으로 쪼갠다. 짝수 개일 때는 정확히 절반, 홀수 개일 때는 앞쪽의 카드들의 수가 더 많도록 슬라이싱한다.
    a_list = string[:length] 
    b_list = string[length:]
    a_flag = True
    b_flag = True
    while True:
        if a_flag == False and b_flag == False: #둘 다 카드가 없다면, 탈출
            break
        if a_list: #앞의 카드들이 하나도 없을 때까지,
            a = a_list.pop(0) #맨 앞의 카드부터 꺼내서
            stack.append(a) #스택에 넣는다.
        else:
            a_flag = False #만약 꺼낼 카드가 하나도 없다면 a_list에 카드가 없다는 뜻으로 flag에 False 저장
        if b_list: #뒤의 카드들이 하나도 없을 때까지,
            b = b_list.pop(0) #맨 앞의 카드부터 꺼내서
            stack.append(b) #스택에 넣는다.
        else:
            b_flag = False #만약 꺼낼 카드가 하나도 없다면 b_list에 카드가 없다는 뜻으로 flag에 False 저장

    print("#{} {}".format(test_case, " ".join(map(str, stack))))