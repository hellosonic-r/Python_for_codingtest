import sys

t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    a_list = list(map(int, sys.stdin.readline().split()))

    m = int(input())
    b_list = list(map(int, sys.stdin.readline().split()))

    a_list.sort()
    result = []
    for num in b_list:
        start = 0
        end = n-1 
        ans = False
        while start <= end:
            mid = (start + end) // 2 
            if num < a_list[mid]:
                end = mid-1 
            elif num > a_list[mid]:
                start = mid+1
            else:
                ans = True
                break
    
        if ans:
            result.append(1)
        else:
            result.append(0)

    for i in result:
        print(i)

