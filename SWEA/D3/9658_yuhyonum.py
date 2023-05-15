t = int(input())

for test_case in range(1, t+1):
    n = int(input())
    length = len(list(map(int, str(n))))
    num = round(n / (10**(length-1)), 1)

    if round(num) == 10:
        num = num / 10
        length += 1

    print("#{} {}{}{}{}".format(test_case, num, "*", "10^", length-1))

