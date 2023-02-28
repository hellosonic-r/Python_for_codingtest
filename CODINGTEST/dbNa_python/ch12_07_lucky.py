n = list(map(int, str(input())))
front = 0
back = 0
for i in range(len(n)):
    if i < len(n)//2:
        front += n[i]
    else:
        back += n[i]


print("LUCKY" if front == back else "READY")
