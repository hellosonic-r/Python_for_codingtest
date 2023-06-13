##나의 코드
n, m = map(int, input().split()) #n:나무의 수 m:목표나무의길이
tree = list(map(int, input().split()))
tree.sort() # 10 15 17 20

result = []
## 절단기의 높이를 0~나무의높이의 최대값으로 지정할 수 있음(즉, 0~20)
start = 0 #절단기의 높이의 시작값:0
end = tree[-1] #절단기의 높이의 끝값: 나무의높이의 최대값
 
while start <= end: 
    mid = (start + end) // 2 #절단기의 높이를 중앙값부터 설정
    cutting = 0 #잘랐을 때의 나무의 길이
    for t in tree: #나무의 높이를 저장
        if t >= mid: #설정한 절단기의 높이보다 나무가 크다면 자를 수 있으므로
            cutting += (t-mid) #잘랐을때의 나무의 길이의 총합에 저장
    if cutting >= m: #만약 나무의 길이의 총합이 목표값 이상이라면
        result.append(mid) #결과 리스트에 저장
    if cutting > m: #만약 목표값보다 길게 잘렸다면
        start = mid + 1 #절단기의 높이를 올린다.
    elif cutting < m: #만약 목표값보다 짧게 잘렸다면
        end = mid -1 #절단기의 높이를 낮춘다
    else:
        break

print(max(result))
    

#다른 코드(더 깔끔)
n, m = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree)

result = 0 #높이 최대값을 저장하는 변수
while start <= end:
    mid = (start+end)//2
    log = 0 #잘린 나무의 총합
    for t in tree:
        if t >= mid:
            log += (t-mid)

    if log < m:
        end = mid-1 
    else:
        result = mid #절단기 높이의 최대값을 구하는 것이기 때문에, 여기에 result 저장
        start = mid+1

print(result)


