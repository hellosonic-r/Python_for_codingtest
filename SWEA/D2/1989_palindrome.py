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
            

##다시 풀어보기
t = int(input())

for test_case in range(1, t+1):
    string = list(input())
    if string == string[::-1]:
        print("#{} {}".format(test_case, 1))
    else:
        print("#{} {}".format(test_case, 0))

