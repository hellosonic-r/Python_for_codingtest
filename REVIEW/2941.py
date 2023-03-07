string = str(input())
croatia = ["c=","c-","dz=","d-","lj","nj","s=","z="]

for c in croatia:
    string = string.replace(c,"*")

print(len(string))