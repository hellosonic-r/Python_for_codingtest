t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    if (n - 1) % 2 == 1:
        print("#{} {}".format(test_case, "Alice"))
    else:
        print("#{} {}".format(test_case, "Bob"))
        