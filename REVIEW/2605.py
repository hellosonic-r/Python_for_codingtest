n = int(input())
command = list(map(int, input().split()))
ans = []
for i in range(len(command)): #i = 0,1,2,3,4
    ans.insert(i-command[i], i+1)

print(" ".join(map(str, ans)))