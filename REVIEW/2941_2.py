dic = {"c=":"*", "c-":"*", "dz=":"*", "d-":"*", "lj":"*", "nj":"*", "s=":"*", "z=":"*"}
string = input()

for i in range(len(string)-2):
    if string[i:i+3] in dic:
        string = string.replace(string[i:i+3], dic[string[i:i+3]])

for i in range(len(string)-1):
    if string[i:i+2] in dic:
        string = string.replace(string[i:i+2], dic[string[i:i+2]])
        
print(len(string))


##이렇게 간단히 풀 수도 있다.
string = input()
croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for c in croatia:
    string = string.replace(c, "*")

print(len(string))