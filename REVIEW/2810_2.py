n = int(input())
seat = list(input())

s = seat.count('S')
l = seat.count('L')//2 

if l == 0:
    print(s)
else:
    print(s+l+1)
