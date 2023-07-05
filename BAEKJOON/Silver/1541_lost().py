
s = list(input())

num_list = []
temp = ""
for i in range(len(s)):
    if s[i] == "+" or s[i] == "-":
        if "+" in temp:
            num_list.append(int("".join(map(str,temp[1:]))))
        else:
            num_list.append(int("".join(map(str, temp))))
        temp = ""
    
    temp += s[i]

if "+" in temp:
    num_list.append(int("".join(map(str,temp[1:]))))
else:
    num_list.append(int("".join(map(str, temp))))

min_ans = 1e9

for i in range(len(num_list)):
    for j in range(i+1,len(num_list)):
        num_list[i:j]
        