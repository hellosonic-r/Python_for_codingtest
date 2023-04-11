t = int(input())

for test_case in range(1, t+1):
    m = list(map(int, str(input()))) #[0 0 1 1]
    first = [0] * len(m) # [ 0 0 0 0 ] 
    length = len(m)
    count = 0 
    for i in range(length):
        if first[i] != m[i]:
            count += 1
            for j in range(i, length):
                first[j] = m[i]
        else:
            continue
        
    print("#{} {}".format(test_case, count))