##내풀이
n, m = map(int, input().split())
num_list = list(map(int, input().split()))

num_list.sort()

start = num_list[0]
end = num_list[-1] 

while (start<=end):
    temp = 0
    mid = (start + end) // 2
    for i in range(n):
        if num_list[i] >= mid:
            temp += (num_list[i] - mid)

    if temp == m:
        break
    elif temp > m:
        start = mid + 1
    else:
        end = mid - 1

print(mid)


##교재풀이
n, m = map(int, input().split())
num_list = list(map(int, input().split()))

num_list.sort()

start = 0
end = num_list[-1]

result = 0

while (start<=end):
    temp = 0
    mid = (start + end) // 2
    for i in range(n):
        if num_list[i] >= mid:
            temp += (num_list[i] - mid)

    if temp < m: #절단기 높이가 작을때 
        end = mid - 1
    else:
        result = mid 
        start = mid + 1

print(result)
