n = int(input())
num_list = []

for i in range(1, n+1):
    num_list.append(list(map(int,str(i))))
     
ans = []
check = [3, 6, 9]
for i in range(n):
    clap = ""
    for j in num_list[i]:
        if j in check:
            clap += "-"
    if clap == "":
        ans.append(i+1)
    else:
        ans.append(clap)

for i in ans:
    print(i,end=" ")