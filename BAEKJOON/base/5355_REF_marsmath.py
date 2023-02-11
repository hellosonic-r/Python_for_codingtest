T = int(input())

for i in range(T):
    mars_cal = list(map(str, input().split()))
    result = float(mars_cal[0]) # 리스트의 첫 번째 문자열을 result에 저장
    for j in range(len(mars_cal)):
        if mars_cal[j] == '@':
            result = result * 3
        elif mars_cal[j] == '%':
            result = result + 5
        elif mars_cal[j] == '#':
            result = result - 7
    print("%0.2f" % result)