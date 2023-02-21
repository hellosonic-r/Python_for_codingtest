t = int(input())
s = []
for i in range(t):
    s.append(input())


def recursion(s,l,r):
    global count
    count+=1
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return recursion(s, l+1, r-1)

  
def isPalindrome(s):
    return recursion(s,0,len(s)-1)

# for in_s in s:
#     count = 0
#     print(isPalindrome(in_s), count)

for in_s in s:
    count = 0
    print(recursion(in_s,0,len(in_s)-1),count)
