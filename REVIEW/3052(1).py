num_list = []

for _ in range(10):
    num_list.append(int(input())%42)

print(len(list(set(list(num_list)))))
