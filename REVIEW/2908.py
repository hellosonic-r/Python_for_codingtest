###상수
##내풀이
# a, b = map(int, input().split())

# a_list = list(map(int, str(a)))
# b_list = list(map(int, str(b)))

# a_list[0],a_list[2] = a_list[2],a_list[0]
# b_list[0],b_list[2] = b_list[2],b_list[0]

# A = a_list[0] * 100 + a_list[1] * 10 + a_list[2]
# B = b_list[0] * 100 + b_list[1] * 10 + b_list[2]
# print(max)

##다른풀이
a, b = input().split() #734 banana

a = int(a[::-1]) 
print(a) # >> 437
b = str(b[::-1])
print(b) # >> ananab