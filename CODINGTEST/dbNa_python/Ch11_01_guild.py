###모험가 길드
n = int(input())
x = list(map(int, input().split()))

result = 0
count = 0

for i in x: #1 2 2 2 3 
    count += 1 
    if count >= i:
        result += 1
        count = 0

print(result)


