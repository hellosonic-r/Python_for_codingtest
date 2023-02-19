###게임 개발
##나의 풀이
import sys
n, m = map(int, input().split()) #맵의 세로 : n 가로 : m
a,b,d = map(int, input().split()) #a,b : 캐릭터의 현재 위치 / d : 방향
data_list = []
# d = 0:북쪽 1:동쪽 2:남쪽 3:서쪽
for _ in range(n):
    data = list(map(int, sys.stdin.readline().split()))
    data_list.append(data)
print(data_list)

#북쪽 보고 있을때
for i in range(4):
    step = 0
    if a-1 != 0 and 
    

#1,1 현재 위치에서 0을 보고 있는데
#for 네방향
#if (1단계)왼쪽 방향에 가보지 않은 칸 있으면 
    #왼쪽 방향으로 회전한 다음 왼쪽으로 한칸 전진
#elif 왼쪽 방향에 가보지 않은 칸 없으면(다 가봤으면)
    #왼쪽 방향으로 회전만 하고 다시 If 초기로

#If 네 방향 모두 이미 가본 칸, 바다칸인 경우 한칸 뒤로 가고 1단계로
