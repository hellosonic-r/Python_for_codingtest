string = list(input())
alphabet = []
num = 0
for i in range(len(string)):
    if 65 <= ord(string[i]) <= 90:
        alphabet.append(string[i])
    else:
        num += int(string[i])
alphabet.sort()

for i in range(len(alphabet)):
    print(alphabet[i],end = "")
print(num)