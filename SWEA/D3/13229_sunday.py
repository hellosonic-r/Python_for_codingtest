t = int(input())
for test_case in range(1,t+1):
    seven_days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    today = input()
    ans = 6 - seven_days.index(today)
    if ans == 0:
        ans = 7
    print("#{} {}".format(test_case, ans))