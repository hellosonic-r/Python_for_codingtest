##DFS 풀이 (143ms)
def dfs(count, num): #count:숫자 이동횟수 / num:이동한 숫자
    global ans
    if num == 0: #이동한 숫자가 0이라면
        ans = 1 #ans 값을 1로 갱신
        return #리턴해주어야 더이상 실행하지 않음
    if count == 5: #한 번에 5회까지 반복. 이것이 한 사이클
        return 
    x = num_list.pop(0) #1.리스트의 맨 앞 숫자를 x에 저장
    x = x - (count+1) #2.x를 1부터 5까지 순차적으로 뺀다. 처음은 1을 뺌
    if x <= 0: #2-1.만약 뺀 결과가 0 이라면
        x = 0 #2-2. x를 0으로 갱신
    num_list.append(x) #3.리스트 맨 뒤에 감소 완료한 숫자를 추가한다.
    dfs(count+1, x) #dfs 호출 : 감소 후 추가한 숫자를 넘겨준다.

for test_case in range(1, 11):
    t = int(input())
    num_list = list(map(int, input().split()))
    ans = -1
    while True: 
        if ans == 1: #dfs를 통해 ans 값이 바뀔때까지 
            break
        dfs(0, 1) #dfs함수 호출
    print("#{} {}".format(test_case, (" ".join(map(str, num_list)))))


##for문 풀이 (116ms)
for test_case in range(1, 11):
    t = int(input())
    num_list = list(map(int, input().split()))
    check = -1
    while True:
        for i in range(1,6):
            x = num_list.pop(0) #첫 번째 수를 x에 저장
            x = x - i #x를 감소시킨다.

            if x <= 0: #감소시킨 x가 0보다 작거나 같다면
                x = 0 #0으로 갱신
                num_list.append(x) #리스트 마지막에 추가한다.
                check = 1 #마지막에 추가한 값이 0이라면 check에 1 저장
                break #바로 반복문 탈출

            num_list.append(x) #감소시킨 x를 리스트 마지막에 추가
        if check == 1: #check 값이 1이라면, 마지막 숫자가 0이라 중도에 for문을 탈출한 것이므로
            break #while문도 탈출
    print("#{} {}".format(test_case, (" ".join(map(str, num_list)))))
           
            
            
      
        
        