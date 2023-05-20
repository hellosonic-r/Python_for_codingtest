w, h = map(int, input().split()) #가로:w 세로:h
p,q = map(int, input().split())
t = int(input())

#x좌표 구하기
if ((p+t)//w)%2 == 1:
    nx = w-((p+t)%w)
else:
    nx = (p+t)%w

#y좌표 구하기
if ((q+t)//h)%2 == 1:
    ny = h-((q+t)%h)
else:
    ny = (q+t)%h

print(nx, ny)