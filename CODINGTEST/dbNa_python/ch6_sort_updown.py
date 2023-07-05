n = int(input())

num_list = []
for _ in range(n):
    num_list.append(int(input()))
    
num_list.sort(reverse=True)

print(" ".join(map(str, num_list)))
