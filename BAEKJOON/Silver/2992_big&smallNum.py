def dfs(count, temp_list):
    global min_num, ans
    if count == len(x_list): #만약 모든 숫자를 다 사용했을 때,
        if x<int("".join(map(str,temp_list)))<= min_num: #입력값보다 크고, 저장된 최소값보다 작다면
            min_num = int("".join(map(str,temp_list))) #최소값을 갱신한다.
            ans = True #ans를 True로 표시한다.
        return #리턴해준다
    for i in range(len(x_list)):
        if visited[i] == 0: #현재 숫자가 사용되지 않았다면
            visited[i] = 1 #방문 처리하고
            dfs(count+1, temp_list+[x_list[i]]) #숫자 리스트에 추가한다.
            visited[i] = 0 #돌아와서는 방문 처리를 해제한다.
            
x = int(input())
x_list = list(map(int, str(x)))
min_num = 10*10**(len(x_list)-1) #입력값보다 큰 값으로 초기화
visited = [0] * len(x_list)
ans = False #ans = False로 초기화
dfs(0,[])

if ans: #한번이라도 최소값이 갱신되었다면 ans = True이니까
    print(min_num)
else:
    print(0)
