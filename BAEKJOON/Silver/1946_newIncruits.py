##시간초과 - 이중 for문
import sys

t = int(input())
for test_case in range(1,t+1):
    n = int(input())
    result = []
    for _ in range(n):
        result.append(list(map(int, sys.stdin.readline().split())))

    cnt = 0
    for i in range(n): #한 명의 서류, 면접 성적을 뽑는다.
        check = True 
        for j in range(n): #나머지와 서류, 면접 성적을 비교한다.
            if j == i: #만약 비교 대상이 본인이라면
                continue #다음 사람과 비교
            #만약 나머지의 성적과 비교했을 때, 한 번이라도 서류와 면접 순위 둘 다 뒤에 있다면
            if result[i][0] > result[j][0] and result[i][1] > result[j][1]:
                check = False #check 변수에 False 저장하고 반복문을 탈출한다.
                break
        if check: #끝까지 반복이 진행되었다면, 합격이므로
            cnt += 1 #합격자를 카운트한다.

    print(cnt)

'''
1 4
2 3
3 2
4 1
5 5
'''

'''
1 4 max = 4
2 5 x 
3 6 x
4 2 
5 7 x 
6 1 
7 3 x

'''

##틀림 - 정렬
import sys

t = int(input())
for test_case in range(1,t+1):
    n = int(input())
    result = []
    for _ in range(n):
        result.append(list(map(int, sys.stdin.readline().split())))
    result.sort(key = lambda x:x[0])

    bool_cnt = 0
    for i in range(n-1, 0,-1): 
        #조건을 잘못 써서 틀렸다. 이전 사람과만 비교했기 때문에 정확한 답이 아니다.
        if result[i][1] > result[i-1][1]:
            bool_cnt += 1
    print(n - bool_cnt)

'''
1 6  
2 2 
3 4 x
4 3 x
5 1 
6 5
'''

##맞았다 - 정렬
import sys

t = int(input())
for test_case in range(1,t+1):
    n = int(input())
    result = []
    for _ in range(n):
        result.append(list(map(int, sys.stdin.readline().split())))
    result.sort(key = lambda x:x[0]) #서류 성적 오름차순으로 정렬

    bool_cnt = 0 #불합격 사람 수 카운트
    check = result[0][1] 
    for i in range(1, n):
        if result[i][1] > check:
            bool_cnt += 1
        else:
            check = result[i][1]
    print(n - bool_cnt)
