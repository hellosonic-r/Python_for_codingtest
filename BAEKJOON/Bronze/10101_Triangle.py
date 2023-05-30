lst = []
for _ in range(3):
    lst.append(int(input()))
s_lst = list(set(lst))
if lst == [60, 60, 60]:
    print("Equilateral")
elif sum(lst) == 180 and len(s_lst) == 2:
    print("Isosceles")
elif sum(lst) == 180 and len(s_lst) == 3:
    print("Scalene")
elif sum(lst) != 180:
    print("Error")
