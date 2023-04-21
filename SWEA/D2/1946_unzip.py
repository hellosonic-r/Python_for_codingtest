t = int(input())
for test_case in range(1,t+1):
    n = int(input())
    print("#{}".format(test_case))
    c_list = []
    for _ in range(n):
        c, k = map(str, input().split())
        k = int(k)
        c_list += [c]*k
    for i in range(len(c_list)):    
        print(c_list[i],end="")
        if (i+1)%10 == 0:
            print()
    print()
        