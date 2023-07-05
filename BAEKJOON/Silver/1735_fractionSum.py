##시간초과
# a_up, a_down = map(int,input().split()) #a의 분자/분모
# b_up, b_down = map(int,input().split()) #b의 분자/분모

# gcd = 1
# for i in range(max(a_down, b_down),0,-1):
#     if a_down % i == 0 and b_down % i == 0:
#         gcd = i
#         break

# ans_down = a_down * b_down // gcd #분모 
# a_up = a_up*(ans_down//a_down)
# b_up = b_up*(ans_down//b_down)
# ans_up = a_up + b_up

# ans_gcd = 1
# for i in range(max(ans_down, ans_up),0,-1):
#     if ans_down % i == 0 and ans_up % i == 0:
#         ans_gcd = i
#         break

# print(ans_up//ans_gcd, ans_down//ans_gcd)



##시간초과
a_up, a_down = map(int,input().split()) #a의 분자/분모
b_up, b_down = map(int,input().split()) #b의 분자/분모

ans_down = a_down * b_down
ans_up = (a_up * (ans_down // a_down)) + (b_up * (ans_down // b_down))

mid = max(ans_down, ans_up) // 2

gcd = 1
for i in range(mid, 0, -1):
    if ans_down % i == 0 and ans_up % i == 0:
        gcd = i
        break

print(ans_up//gcd, ans_down//gcd)