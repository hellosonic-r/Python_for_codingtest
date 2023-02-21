import sys
import math

a, b, c = map(int, sys.stdin.readline().split())

if a == b == c:
    print(10000 + 1000 * a)
elif a != b != c:
    print(max(a,b,c) * 100)
else:
    if a == b != c:
        print(1000 + a * 100)
    elif a == c != b:
        print(1000 + a * 100)
    elif b == c != a:
        print(1000 + b * 100)
    elif b == a != c:
        print(1000 + b * 100)
    elif c == a != b:
        print(1000 + c * 100)
    elif c == b != a:
         print(1000 + c * 100)
