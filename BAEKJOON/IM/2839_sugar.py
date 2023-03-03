###설탕배달
##내풀이
n = int(input())

bong = [5,3]

five_count = n // bong[0] #n = 17 / five_count = 17//5 =3
# n = 6 /five_count = 1
count = 0 
for i in range(five_count,-1,-1):
    if (n - (bong[0] * i)) % bong[1] == 0: 
        count = i + ((n - (bong[0] * i )) // bong[1])  
        break

if count > 0:
    print(count)
else:
    print(-1)

##다른사람풀이
n = int(input())
bag= 0
while n>=0:
    if n %5==0:
        bag+=n//5
        print(bag)
        break
    n-=3
    bag+=1
else:
    print(-1)

