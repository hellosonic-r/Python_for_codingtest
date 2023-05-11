n, k = map(int, input().split()) #1~n번까지. k번째 사람

num_list = list(range(1, n+1))
stack = []
start = 0
while num_list:
    start = (start + k-1)%len(num_list)
    stack.append(num_list.pop(start))

print("<",end="")
print(", ".join(map(str, stack)), end ="")
print(">")