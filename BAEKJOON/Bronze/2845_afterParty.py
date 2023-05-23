n, k = map(int,input().split())

num_list = list(map(int, input().split()))

for i in range(len(num_list)):
    print((num_list[i] - n*k),end = " ")

print()

