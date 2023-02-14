word = input() #soon

word_rev = word[::-1] #역순이 된다.

print(word_rev) #noos
print(type(word_rev)) #type은 str

print(1 if word == word_rev else 0)