s = list(map(str, str(input()))) #baekjoon
#s[0]-97 = 1  / loc[1] = i
loc = [-1] * 26
for i in range(len(s)):
    if loc[ord(s[i])-97] == -1: 
        loc[ord(s[i])-97] = i
    else:
        continue

for j in range(len(loc)): 
    print(loc[j],end = " ")
    if j == len(loc)-1:
        print()

