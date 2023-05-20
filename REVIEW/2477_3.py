k = int(input())
m_list = []
d_list = []
for _ in range(6):
    d, m = map(int, input().split())
    m_list.append(m)
    d_list.append(d)
big = []
for i in range(len(d_list)):
    if d_list.count(d_list[i]) == 1:
        big.append(i)

big_size = m_list[big[0]] * m_list[big[1]]
small = []
for i in big:
    small.append((i+3)%6)

small_size = m_list[small[0]] * m_list[small[1]]

print((big_size-small_size)*k)