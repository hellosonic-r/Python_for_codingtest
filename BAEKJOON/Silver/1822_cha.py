n, m = map(int, input().split())
a_list = set(list(map(int, input().split())))
b_list = set(list(map(int, input().split())))

print(len(a_list-b_list))
arr = list(a_list-b_list)
arr.sort()
print(" ".join(map(str, arr)))

