v = []

for _ in range(10):
    num = int(input())
    if (num % 42) not in v:
        v.append(num % 42)

print(len(v))