n = int(input())
string = list(input())
if "L" in string:
    cnt = 1
else:
    cnt = 0
i = 0
while i < len(string):
    if string[i] == "S":
        cnt += 1
    elif string[i] == "L":
        cnt += 1
        i += 1
    i+= 1

print(cnt)
