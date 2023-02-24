###음계
ex = [1,2,3,4,5,6,7,8]

num = list(map(int, input().split()))
ex_reversed = sorted(ex, reverse=True)

if num == ex:
    print("ascending")
elif num == ex_reversed:
    print("descending")
else:
    print("mixed")



# a.sort()
# sorted(a)
# sorted(a,reverse = True)
# a.reverse()