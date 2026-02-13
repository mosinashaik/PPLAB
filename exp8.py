word=input("Enter a word:");
vowels={'a','e','i','o','u',
        'A','E','I','O','U'}
found='False'
for ch in word:
    if  ch in vowels:
        found='True'
        break
    if found:
        print("word contains vowels")
    else:
        print("word not contains vowels")
  
