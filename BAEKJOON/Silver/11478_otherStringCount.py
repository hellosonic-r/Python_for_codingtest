##시간초과
s = list(input())

length = len(s)

v = []

for l in range(1,length+1):
    for i in range(length-l+1):
        check = "".join(map(str, s[i:i+l]))
        if check not in v:
            v.append(check)

print(len(v))


##set으로 해결
s = input()
result = set()

for l in range(len(s)):
    for i in range(len(s)-l+1):
        temp = s[i:i+l]
        result.add(temp)

print(len(result))






