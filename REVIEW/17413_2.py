string = list(input())
stack = []
temp_stack = []

i = 0
while i < len(string):
    if string[i] == " ":
        stack.append("".join(map(str, temp_stack[::-1])))
        stack.append(" ")
        temp_stack.clear()
    elif string[i] == "<":
        if temp_stack:
            stack.append("".join(map(str, temp_stack[::-1])))
            temp_stack.clear()
        stack.append(string[i])
        while True:
            i+=1
            stack.append(string[i])
            if string[i] == ">":
                break
    else:
        temp_stack.append(string[i])
    i+=1
    if i == len(string):
        stack.append("".join(map(str, temp_stack[::-1])))
        temp_stack.clear()

print("".join(map(str, stack)))
