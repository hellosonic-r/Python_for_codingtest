t = int(input())
for test_case in range(1,t+1):
    n = int(input())
    count = 1
    total_list = []
    while True:
        if len(total_list) == 10:
            break
        n_list = list(map(int ,str(n*count)))
        total_list += n_list
        total_list = list(set(total_list))
        count += 1
    print("#{} {}".format(test_case, n*(count - 1)))
    
        