# def dfs(count, start, temp_list):
#     if count == 6:
#         ans.append(temp_list)
#         return
#     for i in range(start, len(num_list)):
#         dfs(count+1,i+1,temp_list+[num_list[i]])



# while True:
#     num_list = list(map(int,input().split()))
#     if num_list == [0]:
#         break
#     length = num_list.pop(0)
#     num_list.sort()
#     ans = []
#     dfs(0,0,[])
#     for i in ans:
#         print(" ".join(map(str, i)))
#     print()


##다시 풀어보기
def dfs(n, start, temp_list):
    if len(temp_list) == 6: #전달받은 임시 리스트 길이가 6이라면
        result.append(temp_list) #추가
        return
    if n == count:
        return
    for i in range(start, count):
        dfs(n+1, i+1, temp_list + [num_list[i]])

while True:
    num_list = list(map(int, input().split()))
    if num_list == [0]: #0을 입력받는다면 반복문 탈출
        break
    count = num_list.pop(0)
    result = []
    dfs(0,0,[])
    for i in result:
        print(" ".join(map(str, i)))
    print()

