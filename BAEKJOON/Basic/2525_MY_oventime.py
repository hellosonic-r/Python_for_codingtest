hour, minute = map(int, input().split())
oven_time = int(input())

result_minute = minute + oven_time #24분 12분

if result_minute % 60 == 0:
    hour = hour + result_minute // 60
    result_minute = 0
    hour = hour % 24
else: 
    hour = hour + result_minute // 60
    result_minute = (minute + oven_time) % 60
    hour = hour % 24

print(hour, result_minute)