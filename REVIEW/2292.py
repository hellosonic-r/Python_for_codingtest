n = int(input())
i = 0
while True:
    if n > 3*i*(i+1) + 1:
        i+=1 
    else:
        break
print(i+1)

# n = int(input())

# num = 1
# count = 1

# while n > num:
#     num = num + 6 * count
#     count += 1

# print(count)
