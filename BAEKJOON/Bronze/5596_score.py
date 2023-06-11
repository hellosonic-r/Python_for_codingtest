a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

print(max(sum(a_list), sum(b_list)))