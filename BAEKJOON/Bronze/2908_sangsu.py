###상수

# a, b = map(int, input().split())

# a_list = list(map(int, str(a)))
# b_list = list(map(int, str(b)))

# a_list[0],a_list[2] = a_list[2], a_list[0]
# b_list[0],b_list[2] = b_list[2], b_list[0]

# reverse_A = a_list[0]*100 + a_list[1]*10 + a_list[2]
# reverse_B = b_list[0]*100 + b_list[1]*10 + b_list[2]

# print(reverse_A if reverse_A>reverse_B else reverse_B)

##다른 사람 풀이

a,b = map(list, input().split()) #리스트로 입력 ['7', '9', '4'] ['8', '9', '3']

a.reverse()
b.reverse()

a = int(a[0]+a[1]+a[2])
b = int(b[0]+b[1]+b[2])

print(max(a,b))