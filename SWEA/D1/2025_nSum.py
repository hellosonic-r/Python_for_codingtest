def sequence(n):
    if n == 0:
        return 0
    return n + sequence(n-1)

print(sequence(int(input())))