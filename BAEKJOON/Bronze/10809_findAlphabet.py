find = [-1] * 26

string = input()
string_list = list(map(str, str(string))) #[b a e k j o o n]

for i in range(len(string_list)): # i = 0 
    if find[ord(string_list[i])-97] == -1:
        find[ord(string_list[i])-97] = find[ord(string_list[i])-97] + 1 + i  # string_list[0] = b / 1 


for i in range(len(find)):
    print(find[i],end=" ")
    if i == len(find)-1:
        print()



