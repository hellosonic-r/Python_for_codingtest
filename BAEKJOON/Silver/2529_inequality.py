def dfs(start, idx, temp_list):
    global max_result,min_result,max_ans,min_ans
    if idx == k: #idx:부등호를 저장한 리스트 
        #최소 문자열이라면 최소 문자열을 갱신 후 리턴
        if min_result > int("".join(map(str,temp_list))):
            min_result = int("".join(map(str,temp_list)))
            min_ans = "".join(map(str,temp_list))
        #최대 문자열이라면 최대 문자열을 갱신 후 리턴
        if max_result < int("".join(map(str,temp_list))):
            max_result = int("".join(map(str,temp_list)))
            max_ans = "".join(map(str,temp_list))
        return
    
    for i in range(len(num_list)):
        if visited[i] == 0: #만약 방문 안한 숫자(사용하지 않은 숫자) 중
            if sign[idx] == ">": #">"부등호가 온다면
                if num_list[i] < start: #start변수보다 작은 것이라면
                    visited[i] = 1 #방문 처리하고
                    #start변수보다 작은 숫자를 dfs 변수에 넣고 호출한다
                    dfs(num_list[i], idx+1, temp_list+[num_list[i]])
                    #돌아와서는 방문처리 해제
                    visited[i] = 0
            if sign[idx] == "<": #"<"부등호가 온다면
                if num_list[i] > start: #start변수보다 큰 것이라면
                    visited[i] = 1 #방문 처리하고
                    #start변수보다 큰 숫자를 dfs 변수에 넣고 호출한다
                    dfs(num_list[i], idx+1, temp_list+[num_list[i]]) 
                    #돌아와서는 방문처리 해제
                    visited[i] = 0
            
k = int(input())
sign = list(input().split())

num_list = list(range(0,10))

#max_result,min_result는 최대값, 최소값을 찾기 위한 변수
max_result = 0
min_result = 9876543210
#max_ans,min_ans는 출력을 위한 변수
max_ans = ""
min_ans = ""

#start 시작점(정답 문자열의 첫번째 숫자)을 정해주는 for문 
for i in range(10):
    visited = [0] * 10
    num_list = list(range(0,10))
    starting = num_list.pop(i)
    dfs(starting, 0, [starting])

print(max_ans, min_ans, sep="\n")