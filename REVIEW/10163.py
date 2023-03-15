n = int(input())

total = [[0] * 1001 for _ in range(1001)]

for i in range(1,n+1):
    a,b,w,h = map(int, input().split())
    for j in range(b,b+h): #바뀐부분
        total[j][a:(a+w)] = [i]*w #바뀐부분

for i in range(1,n+1):
    result = 0
    for j in range(1001):
        result += total[j].count(i)
    print(result)


