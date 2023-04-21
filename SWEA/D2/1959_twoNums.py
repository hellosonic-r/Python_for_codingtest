###아니 문제를 잘못읽었네.. 위치만 바꾸는 거였네..

def dfs(x,temp_list):
    if x == len(short_list):
        result.append((temp_list))
        return
    for i in range(len(long_list)):
        if visited[i] == 0:
            visited[i] = 1
            dfs(x+1,temp_list+[long_list[i]])
            visited[i] = 0

t = int(input())
for test_case in range(1,t+1):
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    if len(a_list) > len(b_list):
        long_list = a_list
        short_list = b_list
    else:
        long_list = b_list
        short_list = a_list
    visited = [0] * len(long_list)
    result = []
    dfs(0,[])
    
    max_ans = 0

    for check in result:
        ans = 0
        for i in range(len(short_list)):
            ans += check[i] * short_list[i]
        if max_ans < ans:
            max_ans = ans

    print(max_ans)


### 문제 잘 읽고 정답판정 받은 코드
t = int(input())
for test_case in range(1,t+1):
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    if len(a_list) > len(b_list):
        short_list = b_list
        long_list = a_list
    else:
        short_list = a_list
        long_list = b_list
    k = len(long_list) - len(short_list) + 1
    
    max_ans = 0
    for i in range(k):
        ans = 0
        for j in range(len(short_list)):
            ans += short_list[j] * long_list[j+i]
        if max_ans < ans:
            max_ans = ans
    print("#{} {}".format(test_case, max_ans))


t = int(input())
for test_case in range(1, t+1):
    n, m = map(int,input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))

    #긴 문자열, 짧은 문자열 정하기
    if len(a_list) < len(b_list):
        short_list = a_list
        long_list = b_list
    else:
        short_list = b_list
        long_list = a_list
    
    ans = []
    #긴 문자열의 길이 - 짧은 문자열의 길이 + 1 만큼 움직일 수 있다.
    for i in range(len(long_list)-len(short_list)+1):
        result = 0
        #움직인 각 자리를 곱해서 더해준다.
        for j in range(len(short_list)):
            result += short_list[j] * long_list[j+i]
        ans.append(result)

    print("#{} {}".format(test_case, max(ans)))
        