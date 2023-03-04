n, k = map(int,input().split())

circle = list(range(1,n+1))

josephus = []
i = k-1
while circle:
    josephus.append(circle.pop(i%n)) 
    #(3-1)%7 = 2 /
    #4 % 6 = 4 /6 % 5 =1 / 3%4 = 3 /  5%3 = 2
    i = (i%n)+k-1
    n -= 1

print("<",end ="")
for i in range(len(josephus)):
    if i <= len(josephus)-2:
        print(josephus[i],end =", ")
    elif i == len(josephus)-1:
        print(josephus[i],end="")
print(">")