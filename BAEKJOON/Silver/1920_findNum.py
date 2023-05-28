n = int(input())
a = list(map(int, input().split()))
a.sort() #비교 대상 리스트 정렬 

m = int(input())
b = list(map(int, input().split()))

for x in b:
    start = 0 #시작 : 인덱스 0 
    end = n-1 #끝 : 마지막 인덱스
    ans = False 
    while start <= end: #start>end가 아닐 때까지 
        mid = (start + end) // 2 #중간값을 찾는다.
        if x > a[mid]: #찾는 값이 중간값보다 크다면, 
            start = mid + 1 #다음 반복 시에 중간값 이후의 값 부터 찾는다.
        elif x < a[mid]: #찾는 값이 중간값보다 작다면,
            end = mid - 1 #다음 반복 시에 중간값 이전의 값 부터 찾는다.
        else: #찾는 값이 중간값이라면,
            ans = True #찾는 값이 있으므로 ans = True로 갱신해주고,
            break #반복문을 탈출한다.
    if ans:
        print(1)
    else:
        print(0)