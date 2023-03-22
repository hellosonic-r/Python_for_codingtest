# string = input()

# if 65<= ord(string) <=70:
#     print(ord(string)-55)
# else:
#     print(int(string))

# string = list(input())

# ans = 1
# for i in string:
#     if 65<=ord(i)<=70:
#         ans *= (ord(i) - 55)
#     else:
#         ans *= int(i)

# print(ans)

# print(int(input(),16))

string = list(input())

ans = 0
for i in range(-1,-(len(string))-1,-1):
    if 65<=ord(string[i])<=70:
        ans += (ord(string[i]) - 55) * (16**abs(i+1)) 
    else:
        ans += int(string[i]) * (16**abs(i+1))

print(ans)

