n = int(input())
s = list(map(int, input().split()))
s.sort()
d = {} #개수 담을 딕셔너리 생성
for i in range(len(s)):
    if s[i] not in d: #만약 딕셔너리에 없다면
        d[s[i]] = 1 #해당 값에 카운트 1
    else: #만약 이미 딕셔너리에 있다면
        d[s[i]] += 1 #해당 값에 카운트 += 1

m = int(input())
num_list = list(map(int, input().split()))

result = []

#이분탐색 시작
for x in num_list: #두 번째 숫자리스트에 있는 값을 하니씩 확인
    start = 0 #시작 인덱스 : 0
    end = n-1 #끝 인덱스 : n-1
    ans = False #ans에 False 저장(이분탐색이 끝난 후에도 False가 저장되어 있다면 result에 0 저장)
    while start <= end:
        mid = (start + end) // 2
        if x < s[mid]:
            end = mid-1
        elif x > s[mid]:
            start = mid+1
        else: #만약 첫 번재 숫자리스트에 숫자가 있다면, 
            ans = True #ans를 True로 갱신
            break
    if ans: #ans가 갱신된다면,
        result.append(d[s[mid]]) #목표값에 해당하는 딕셔너리 추가 
    else:
        result.append(0)

print(" ".join(map(str, result)))

