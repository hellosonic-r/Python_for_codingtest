t = int(input())
for test_case in range(1, t+1):
    string = list(input())
    i = 0
    ans = -1
    while True:
        if i > (len(string) // 2):
            ans = 1
            break
        if string[i] != string[-(i+1)]:
            ans = 0
            break
        i += 1
        
    print("#{} {}".format(test_case, ans))
            