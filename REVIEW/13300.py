n, k = map(int, input().split()) #n:총 학생 수, k:최대 인원수
girl = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0} #최대 인원이 3일때 5명이면 
boy = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
for _ in range(n):
    s,y = map(int, input().split()) #여:0 / 남:1
    if s == 0:
        girl[y] += 1
    elif s == 1:
        boy[y] += 1
cnt = 0
for i in range(1,7):
    if girl[i] % k == 0:
        cnt += girl[i] // k
    else:
        cnt += (girl[i] // k + 1)
    if boy[i] % k == 0:
        cnt += boy[i] // k
    else:
        cnt += (boy[i] // k + 1)

print(cnt)