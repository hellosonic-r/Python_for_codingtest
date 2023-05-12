light = ["N"] + list(input())
length = len(light) #7
i = 1
ans = 0
while True:
    if light == ["N"] * length:
        break
    if i == length:
        ans = -1
        break
    if light[i] == "Y":
        ans += 1
        for j in range(1,length):
            if j%i == 0:
                if light[j] == "Y":
                    light[j] = "N"
                elif light[j] == "N":
                    light[j] = "Y"
    i += 1

print(ans)