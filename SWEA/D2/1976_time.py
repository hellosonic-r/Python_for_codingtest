t = int(input())
for test_case in range(1, t+1):
    h1,m1,h2,m2 = map(int, input().split())
    m3 = m1 + m2
    h3 = 0
    if m3 >= 60:
        h3 += 1
        m3 = m3%60
    h3 = h3 + h1+h2
    if h3 >= 13:
        h3 = h3 - 12
    print("#{} {} {}".format(test_case, h3, m3 ))