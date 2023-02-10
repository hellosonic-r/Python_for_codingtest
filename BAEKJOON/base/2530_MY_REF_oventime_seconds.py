hour, minute, second = map(int, input().split())
time = int(input())

result_second = (time + second) % 60
result_minute = minute + (second + time) // 60
result_hour = hour + (minute + (second + time) // 60) // 60

if result_hour >= 24:
    result_hour = result_hour % 24 #이 부분 ref 참고하여 수정함
if result_minute >= 60:
    result_minute = result_minute % 60

print('{} {} {}'.format(result_hour, result_minute, result_second))