#킹의 위치, 돌의 위치, 움직이는 횟수
k_input, s_input, n = input().split()
king = list(map(str, str(k_input)))
stone = list(map(str, str(s_input)))
k = [ord(king[0])-65, int(king[1])-1]
s = [ord(stone[0])-65, int(stone[1])-1]
n = int(n)

board = [[0]*8 for _ in range(8)]
d = {"R":0, "L":1, "B":2, "T":3, "RT":4, "LT":5, "RB":6, "LB":7}

dx = [1,-1,0,0,1,-1,1,-1]
dy = [0,0,-1,1,1,1,-1,-1]

command = []
for _ in range(n):
    command.append(input())

for c in command:
    k_nx = k[0] + dx[d[c]]
    k_ny = k[1] + dy[d[c]]
    if 0<=k_nx<8 and 0<=k_ny<8: #킹이 범위상으로 다음으로 이동 가능
        if k_nx == s[0] and k_ny == s[1]: #킹 이동방향에 돌이 있을 경우
            s_nx = s[0] + dx[d[c]]
            s_ny = s[1] + dy[d[c]]
            if 0<=s_nx<8 and 0<=s_ny<8: #돌이 갈 수 있다면
                k = [k_nx, k_ny]
                s = [s_nx, s_ny]
        else: #킹 이동 방향에 돌이 없을 경우
            k = [k_nx, k_ny]


print((chr(k[0]+65))+str(k[1]+1))
print((chr(s[0]+65))+str(s[1]+1))

