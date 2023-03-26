##내 풀이 - 시간초과
import sys
n = int(input())

all = []
for _ in range(n):
    all.append(list(map(int, sys.stdin.readline().split())))

for i in range(len(all)):
    ans = 1
    cnt = 1
    meeting = []
    meeting.append(all[i])
    for j in range(len(all)):
        if j == i:
            continue
        else:
            tmp_cnt = 0
            for k in range(len(meeting)):
                if meeting[k][0] < all[j][0] < meeting[k][1]\
                      or meeting[k][0] < all[j][1] < meeting[k][1]:
                    continue
                else:
                    tmp_cnt +=1
            if tmp_cnt == len(meeting):
                meeting.append(all[j])
                cnt += 1
    if cnt > ans:
        ans = cnt

print(ans)


## 다른 사람 코드 
n = int(input())
time = []

for _ in range(n):
    start, end = map(int, input().split())
    time.append((start,end))

#시작 시각을 기준으로 오름차순 정렬
time = sorted(time, key=lambda a: a[0])
#끝나는 시각을 기준으로 오름차순 정렬
time = sorted(time, key=lambda a: a[1])

cnt = 1
last = time[0][1]
for i in range(1, n):
    #다음 회의 시간의 시작시각이 이전 회의의 끝나는시각보다 크거나 같다면
    if time[i][0] >= last:
        #회의 가능
        cnt += 1
        #끝나는시각을 다음 회의의 끝나는시각으로 갱신
        last = time[i][1]

print(cnt)