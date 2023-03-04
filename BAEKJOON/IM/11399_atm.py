n = int(input())
p = list(map(int, input().split()))

p.sort()

fin = 0
result = 0
for i in range(len(p)):
    result = result + p[i] 
    fin = result + fin
    
print(fin)