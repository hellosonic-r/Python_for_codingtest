##시간초과
t = int(input())

for test_case in range(1, t+1):
    n = int(input()) #정수의 개수
    num = ""
    while True:
        num += "".join(map(str, input().split()))
        if len(num) == n:
            break
    num_list = list(map(int, str(num)))
    result = []
    for i in range(1, len(num_list)+1): # i = 1,2,3
        for j in range(len(num_list)+1 - i):
            if int("".join(map(str, num_list[j:j+i]))) not in result:
                result.append(int("".join(map(str, num_list[j:j+i]))))

    answer = -1
    for i in range(max(result)+1):
        if i not in result:
            answer = i
            break

    print("#{} {}".format(test_case, answer))



##이렇게 푸는거구나..
t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    num = ""
    while True:
        num += "".join(map(str, input().split())) #공백을 포함한 문자를 입력받는다.
        if len(num) == n: #문자열의 길이가 n이되면 입력 반복문 탈출
            break
    check = 0 
    while True: #0부터 문자열에 있는지 찾는다.
        if str(check) not in num:
            break
        check += 1

    print("#{} {}".format(test_case, check))

