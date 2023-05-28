n = int(input())
n_list = list(map(int, str(n)))
n_list.sort(reverse=True)

print(int("".join(map(str, n_list))))