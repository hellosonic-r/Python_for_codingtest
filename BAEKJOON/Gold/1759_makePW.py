def dfs(count, start, temp_list):
    if len(temp_list) == l: #temp_list 길이가 l에 도달한다면
        mo_cnt = 0
        za_cnt = 0
        for i in temp_list:
            if i in mo: #모음 개수 체크
                mo_cnt += 1
            if i in za: #자음 개수 체크
                za_cnt += 1
        if mo_cnt >= 1 and za_cnt >= 2:
            ans.append(temp_list) #조건에 맞다면 ans에 추가
    if count == c:
        return
    
    #for문의 시작점을 start로 정해놓고
    #하위 함수 호출 시 start+1을 받아서 중복되지 않게 만듬
    for i in range(start, len(pw_list)): 
        dfs(count+1, i+1, temp_list+[pw_list[i]])

l, c = map(int, input().split())
pw_list = list(map(str, input().split()))
pw_list.sort()
mo = []
za = []
for i in pw_list:
    if i in ['a','e','i','o','u']:
        mo.append(i) #모음 리스트 생성
    else:
        za.append(i) #자음 리스트 생성
ans = []

dfs(0,0,[])
for i in ans:
    print("".join(map(str, i)))