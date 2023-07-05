n = int(input())
ans = [-1] * n 
num_list = list(map(int,input().split()))

for i in range(len(num_list)):
    cnt = 0
    idx = 0
    for j in range(len(ans)):
        if ans[j] == -1:
            cnt += 1
        if cnt == num_list[i]:
            idx = j+1
            break

    for k in range(idx, len(ans)):
        if ans[k] == -1:
            ans[k] = i+1
            break

print(" ".join(map(str, ans)))