n, k = map(int, input().split())
room_boy = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
room_girl = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
for _ in range(n):
    s, y = map(int, input().split())
    if s == 1:
        room_boy[y] += 1
    else:
        room_girl[y] += 1

cnt = 0
for i in range(1,7):
    if room_boy[i] % k == 0:
        cnt += room_boy[i]//k
    else:
        cnt += (room_boy[i]//k) +1
    if room_girl[i] % k == 0:
        cnt += room_girl[i]//k
    else:
        cnt += (room_girl[i]//k) +1

print(cnt)

