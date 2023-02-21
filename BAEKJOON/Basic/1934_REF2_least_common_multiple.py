import sys

n = int(sys.stdin.readline())

for _ in range(n):

    num_1, num_2 = map(int,sys.stdin.readline().strip().split(" "))

    a = set([i for i in range(1, num_1 - num_1 // 2 + 1) if num_1 % i ==0] + [num_1])
    b = set([i for i in range(1, num_2 - num_2 // 2 + 1) if num_2 % i ==0] + [num_2])
    gt_div = max(list(a & b))
    lt_mul = num_1 * num_2 // gt_div
    print(lt_mul)