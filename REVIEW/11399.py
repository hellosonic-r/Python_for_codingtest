# n = int(input())
# time = list(map(int, input().split()))

# time.sort()

# result = 0
# time_temp = 0
# for i in range(n):
#     time_temp += time[i]
#     result += time_temp

# print(result)

###다른 풀이
n = int(input())
time = list(map(int, input().split()))

time.sort()

result = 0
for i in range(1,n+1):
    result += sum(time[0:i])

print(result) 
