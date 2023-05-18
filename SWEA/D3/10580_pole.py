##1
t = int(input())

for test_case in range(1,t+1):
    n = int(input())
    line = []
    cnt = 0
    for _ in range(n):
        start, end = map(int, input().split())
        line.append((start, end)) #입력한 전선 정보들을 리스트에 추가

    #하나씩 꺼내어 보면서
    for a,b in line:
        for x,y in line:
            #조건에 맞으면 카운트 해준다.
            if a<x and b>y:
                cnt += 1
            elif a>x and b<y:
                cnt += 1

    #a전선과 b를 비교할 경우, b전선과 a전선을 비교할 경우는 같으므로 2로 나눈다.
    print("#{} {}".format(test_case, cnt//2)) 


##2
t = int(input())

for test_case in range(1,t+1):
    n = int(input())
    line = []
    cnt = 0
    for _ in range(n):
        start, end = map(int, input().split())
        #전선을 하나씩 입력받을 때마다 기존에 있던 전선들과 비교한다.
        for a,b in line:
            if start<a and end>b:
                cnt += 1
            elif start>a and end<b:
                cnt += 1

        line.append((start,end))

    print("#{} {}".format(test_case, cnt))

