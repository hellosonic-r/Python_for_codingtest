t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    num_list = list(map(int, input().split()))
    num_list.sort()
    print("#",test_case,sep="",end=" ")
    print(" ".join(map(str, num_list)))
    