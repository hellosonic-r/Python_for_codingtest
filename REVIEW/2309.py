dwarfs = []
for _ in range(9):
    dwarfs.append(int(input()))

fake_sum = sum(dwarfs) - 100
fake_dwarfs = []
for i in range(9):
    for j in range(i+1,9):
        if dwarfs[i] + dwarfs[j] == fake_sum:
            fake_dwarfs.append(dwarfs[i])
            fake_dwarfs.append(dwarfs[j])

dwarfs.pop(dwarfs.index(fake_dwarfs[1]))
dwarfs.pop(dwarfs.index(fake_dwarfs[0]))

dwarfs.sort()
for real_dwarfs in dwarfs:
    print(real_dwarfs)
