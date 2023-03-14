n = int(input())

sugar = [3, 5]

for i in range(n//sugar[1],-1,-1): #3,2,1,,,,0
    if (n - (i*sugar[1])) % sugar[0] == 0:
        print(i + (n-(i*sugar[1])) // sugar[0])
        break
    if i == 0:
        if n % sugar[0] == 0:
            print(n//sugar[0])
        else:
            print(-1)



