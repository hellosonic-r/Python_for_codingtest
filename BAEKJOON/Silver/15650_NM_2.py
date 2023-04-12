s = []

def check_sort(num_list):
    for i in range(len(num_list)-1):
        if num_list[i+1] - num_list[i] > 0:
            continue
        else:
            return False
    return True

def dfs():
    if len(s) == m:
        if check_sort(s):
            print(" ".join(map(str, s)))
            return
        else:
            return 

    for i in range(1, n+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()

n, m = map(int, input().split())

dfs()
