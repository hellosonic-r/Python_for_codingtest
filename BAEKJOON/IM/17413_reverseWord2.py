string = list(input())

i = 0
start = 0

while i < len(string):
    if string[i] == "<":
        while string[i] != ">":
            i += 1
        i += 1
    elif string[i].isalnum():
        start = i
        while i < len(string) and string[i].isalnum():
            i += 1
        tmp = string[start:i]
        tmp.reverse()
        string[start:i] = tmp
    else:
        i += 1

print("".join(string))

