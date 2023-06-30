s = input()

cnt0 = 0
cnt1 = 0
stack0 = []
stack1 = []

for i in range(len(s)):
    if s[i] == "0":
        if stack0:
            continue
        else:
            stack0.append(0)
            cnt0 += 1
    else:
        if stack0:
            stack0.pop()
        else:
            continue
        
for i in range(len(s)):
    if s[i] == "1":
        if stack1:
            continue
        else:
            stack1.append(1)
            cnt1 += 1
    else:
        if stack1:
            stack1.pop()
        else:
            continue

print(min(cnt0, cnt1))
