t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    dict = {2:0, 3:0, 5:0, 7:0, 11:0}
    for key in dict.keys():
        while True:
            if n / key != n // key:
                break
            n = n // key
            dict[key] += 1
    print("#{}".format(test_case), end = " ")
    for value in dict.values():
        print(value, end = " ")
    print()
    
        
              