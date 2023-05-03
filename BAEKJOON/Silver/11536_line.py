n = int(input())
string_list = []
for _ in range(n):
    string_list.append(input())

sorted_string = sorted(string_list)
r_sorted_string = sorted(string_list, reverse=True)

if string_list == sorted_string:
    print("INCREASING")
elif string_list == r_sorted_string:
    print("DECREASING")
else:
    print("NEITHER")