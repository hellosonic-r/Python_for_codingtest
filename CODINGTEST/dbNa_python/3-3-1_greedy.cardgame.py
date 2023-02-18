n, m = map(int, input().split())

fin_list = []
for _ in range(n):
    num_list = sorted(list(map(int, input().split())))
    fin_list.append(num_list[0])

print(max(fin_list))