n = int(input())

fib = 0
fib_list = [0,1,1]

for i in range(n-2):
    if i == 0:
        fib = fib_list[i-2] + fib_list[i-1]
        fib_list.append(fib)
    elif i >= 1:
        fib = fib_list[i+1] + fib_list[i+2]
        fib_list.append(fib)

print(fib_list[n])
