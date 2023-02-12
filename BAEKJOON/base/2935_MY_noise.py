a = int(input())
oper = str(input())
b = int(input())

fin = 0
if oper == '*':
    fin = a * b
elif oper == '+':
    fin = a + b

print(fin)