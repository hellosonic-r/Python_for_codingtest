t = int(input())
for test_case in range(1, t+1):
    dict = {50000:0, 10000:0, 5000:0, 1000:0, 500:0, 100:0, 50:0, 10:0}
    n = int(input())
    if n // 50000 >= 1:
        dict[50000] += (n//50000)
        n = n%50000
    if n // 10000 >= 1:
        dict[10000] += (n//10000)
        n = n%10000
    if n // 5000 >= 1:
        dict[5000] += (n//5000)
        n = n%5000
    if n // 1000 >= 1:
        dict[1000] += (n//1000)
        n = n%1000
    if n // 500 >= 1:
        dict[500] += (n//500)
        n = n%500
    if n // 100 >= 1:
        dict[100] += (n//100)
        n = n%100
    if n // 50 >= 1:
        dict[50] += (n//50)
        n = n%50
    if n // 10 >= 1:
        dict[10] += (n//10)
        n = n%10
    print("#{}".format(test_case))
    for value in dict.values():
        print(value, end = " ")
    print()
