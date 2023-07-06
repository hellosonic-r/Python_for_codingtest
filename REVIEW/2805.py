n, m = map(int, input().split())
num_list = list(map(int, input().split()))

start = 1
end = max(num_list)

result = 0

while (start <= end):
    mid = (start + end) // 2
    temp = 0
    for i in range(n):
        if num_list[i] >= mid:
            temp += (num_list[i]-mid)

    if temp < m: #더 잘렸을 때 절단기 높이 낮춰야 함
        end = mid - 1
    else: #더 잘렸을 때 절단기 높이 높여야함 
        start = mid + 1
        result = mid

print(result)

