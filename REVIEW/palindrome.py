#try1
# string = list(input())

# def palindrome(string):
#     if len(string) <= 1:
#         return True
#     if string[0] != string[-1]:
#         return False
#     return palindrome(string[1:-1])

# result = palindrome(string)
# if result == True:
#     print("팰린드롬")
# else:
#     print("팰린드롬아니다")

# #try2
# string = input()

# def palindrome(string):
#     if len(string) <= 1:
#         return True
#     if string[0] != string[-1]:
#         return False
#     return palindrome(string[1:-1])

# result = palindrome(string)
# if result == True:
#     print("팰린")

#try3
string = input()

def palindrome(string):
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False
    return palindrome(string[1:-1])