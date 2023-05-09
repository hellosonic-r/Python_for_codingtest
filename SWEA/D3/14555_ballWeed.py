##내풀이(약간 노가다..)
t = int(input())
for test_case in range(1, t+1):
    string = list(input())
    cnt = 0
    for i in range(len(string)-1):
        if string[i] + string[i+1] == "(|":
            cnt += 1
        if string[i] + string[i+1] == "|)":
            cnt += 1
        if string[i] + string[i+1] == "()":
            cnt += 1
    print("#{} {}".format(test_case, cnt))

##다른 풀이("()"일 경우 임의로 다음 인덱스 통과하도록 설정)
t = int(input())
for test_case in range(1, t+1):
    string = list(input())
    cnt = 0
    i = 0
    while i < len(string):
        if string[i] == "(": #열린 괄호를 만났을 때, 
            if string[i+1] == ")": #다음 문자가 닫힌 괄호라면,
                cnt += 1
                i+=1 #다음 문자는 확인할 필요가 없으므로 인덱스를 추가적으로 증가
            elif string[i+1] == "|":
                cnt +=1
        elif string[i] == ")":
            cnt+=1
        i+=1 #인덱스는 기본적으로 1 만큼 항상 증가 "()" 일 경우엔 한 번 반복에 인덱스 2 증가

    print("#{} {}".format(test_case, cnt))
       