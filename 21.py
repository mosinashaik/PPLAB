from itertools import permutations
words=input("enter a words")
for i in range(1,len(words)):
    for p in permutations(words,i):
        print(" ".join(p))
