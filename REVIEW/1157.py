###단어공부
string = list(input().upper())


string_list = list(set(list(map(str, str(string)))))
cnt = []
for i in range(len(string_list)):
    cnt.append(string.count(string_list[i]))

if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(string_list[cnt.index(max(cnt))]) 

# string = input().upper()

# print(string)

# cnt = string.count("C")
# print(cnt)