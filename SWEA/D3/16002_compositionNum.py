count = 0
def check(a):
    global count
    count = 0
    for i in range(2, a//2 +2):
        if a == 2 and i == 2:
            continue
        if a % i == 0:
            count += 1
            break
    if count != 0:
        return True

t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    x = 2
    y = x + n
    while True:
        if (check(x) == True) and (check(y) == True):
            print("#{} {} {}".format(test_case, y, x))
            break
        else:
            x += 1
            y += 1