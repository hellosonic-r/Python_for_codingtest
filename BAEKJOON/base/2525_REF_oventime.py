hour, minute = map(int, input().split())
time = int(input())

result_minute = (minute + time) % 60 
result_hour = hour + (minute + time) // 60

if result_hour >= 24:
    result_hour -= 24

print('{} {}'.format(result_hour, result_minute))