def dfs(n, temp_list):
    global max_ans
    if n == len(a_list): #a의 길이만큼 숫자를 뽑았다면
        #리스트에 저장된 숫자들을 정수로 바꾸고 다시 리스트에 저장(맨 앞이 0이라면, 리스트 길이가 줄어들 것) 
        #다시 저장한 리스트의 길이가 a의 길이와 차이가 있다면 앞의 숫자가 0이 왔다는 뜻 
        if len(list(map(int,str(int("".join(map(str, temp_list))))))) != len(a_list):
            #그 즉시리턴한다.
            return
        else:
            #만약 그렇지 않다면 최대값을 구한다
            if int("".join(map(str, temp_list))) < b:
                if max_ans < int("".join(map(str, temp_list))):
                    max_ans = int("".join(map(str, temp_list)))

    for i in range(len(a_list)):
        if v[i] == 0:
            v[i] = 1
            dfs(n+1, temp_list + [a_list[i]])
            v[i] = 0

a, b = map(int, input().split()) #b보다 작으면서 가장 큰 값. 0으로 시작하면 안됨
a_list = list(map(int, str(a)))

v = [0] * len(a_list)

max_ans = -1

dfs(0,[])

print(max_ans)


##생각해보니 맨 앞자리가 0이 아닌 경우만 생각해주면 된다.
def dfs(n, temp_list):
    global max_ans
    if n == len(a_list):
        #맨 앞자리 하나만 0인지 아닌지 판단하면 된다.
        if temp_list[0] == 0:
            return
        else:
            if int("".join(map(str, temp_list))) < b:
                if max_ans < int("".join(map(str, temp_list))):
                    max_ans = int("".join(map(str, temp_list)))

    for i in range(len(a_list)):
        if v[i] == 0:
            v[i] = 1
            dfs(n+1, temp_list + [a_list[i]])
            v[i] = 0

a, b = map(int, input().split()) #b보다 작으면서 가장 큰 값. 0으로 시작하면 안됨
a_list = list(map(int, str(a)))

v = [0] * len(a_list)

max_ans = -1

dfs(0,[])

print(max_ans)


