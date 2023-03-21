# t = int(input())
# for _ in range(t):
#     string = list(input().split())
#     for i in range(len(string)):
#         temp_list = list(string[i])
#         temp_list.reverse()
#         for j in range(len(temp_list)):
#             print(temp_list[j], end="")
#             if j == len(temp_list)-1:
#                 print(" ",end="")
#         if i == len(string)-1:
#             print()


# t = int(input())
# for i in range(t):
#     string = list(input().split())
#     for words in string:
#         print(words[::-1], end = " ")
#     print()


t = int(input())

for _ in range(t):
    string = input()
    string += " "
    stack = []
    for i in string:
        if i != " ":
            stack.append(i)
        else:
            while stack:
                print(stack.pop(), end = "")
            print(" ", end = "")
    print()