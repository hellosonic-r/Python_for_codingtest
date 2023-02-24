n = int(input())
string = input()

S_count = string.count("S")
LL_count = string.count("LL")

if "LL" in string:
    print(S_count + LL_count + 1)
else:
    print(S_count)