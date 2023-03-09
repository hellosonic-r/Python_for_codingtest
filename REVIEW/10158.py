w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

x = list(range(w+1))
y = list(range(h+1))

if ((p+t)//w) == 0 or ((p+t)//w) % 2 == 0:
    nx = x[(p+t)%w]  
elif ((p+t)//w) % 2 == 1:
    nx = x[-((p+t)%w)-1]

if ((q+t)//h) == 0 or ((q+t)//h) % 2 == 0:
    ny = y[(q+t)%h]
elif ((q+h)//h) % 2 == 1:
    ny = y[-((q+t)%h)-1]

print(nx,ny)