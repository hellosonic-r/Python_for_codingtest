###예제입력만 맞는 코드
k = int(input())

# 동 서 남 북
arr = []
for i in range(6):
    arr.append(list((map(int, input().split()))))

big_direction = []

check = [0,0,0,0,0]
for i in range(len(arr)):
    check[arr[i][0]]+=1
for i in range(1,len(check)):
    if check[i] == 1:
        big_direction.append(i)

big_value = []
small_value = []

for i in range(len(arr)):
    if arr[i][0] == big_direction[0]:
        big_value.append(arr[i][1])
    elif arr[i][0] == big_direction[1]:
        big_value.append(arr[i][1])


for j in range(len(arr)):
    if arr[j][0] == arr[(j+2)%6][0]:
        small_value.append(arr[(j+1)%6][1])
        small_value.append(arr[(j+2)%6][1])
        break

total = big_value[0] * big_value[1]
small = small_value[0] * small_value[1]

print(k * (total-small))



###정답코드 
k = int(input())

height = []
width = []
total = []

for _ in range(6):
    direction, meter = map(int, input().split())
    if direction == 1 or direction == 2:
        width.append(meter)
        total.append(meter)
    else: 
        height.append(meter)
        total.append(meter)

big = max(height) * max(width)

small_1 = total[(total.index(max(height))+3)%6]
small_2 = total[(total.index(max(width))+3)%6]

print(k*(big-(small_1*small_2)))

