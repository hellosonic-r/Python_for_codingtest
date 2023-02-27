###크로아티아 알파벳
croatia = ["c=","c-","dz=","d-","lj","nj","s=","z="]
string = input()

for i in croatia:
    string = string.replace(i,"*")

print(len(string))