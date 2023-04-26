#변수로 넘겨줄 시
def dfs(count, muscle):
    global ans
    #중량이 500이하 되면 리턴
    if muscle < 500:
        return
    #키트를 다 선택했다면 ans +=1
    if count == n:
        ans+=1
        return

    for i in range(len(kit)):
        #중복된 키트를 사용하지 않기 위해 방문 처리
        if visited[i] == 0:
            visited[i] = 1
            #키트 사용 시 중량을 같이 넘겨준다.
            dfs(count+1, muscle+kit[i]-k)
            #돌아와서는 방문처리 해제
            visited[i] = 0

n,k = map(int, input().split())
kit = list(map(int, input().split()))
visited = [0] * n
ans = 0

dfs(0, 500)
print(ans)

#외부에 리스트 둘 시
def dfs(count):
    global ans
    if sum(muscle_list) < 500:
        return
    if count == n:
        ans+=1
        return

    for i in range(len(kit)):
        if visited[i] == 0:
            visited[i] = 1
            muscle_list.append(kit[i])
            muscle_list.append(-k)
            dfs(count+1)
            visited[i] = 0
            muscle_list.pop()
            muscle_list.pop()


n,k = map(int, input().split())
kit = list(map(int, input().split()))
visited = [0] * n
muscle_list = [500]
ans = 0

dfs(0)
print(ans)