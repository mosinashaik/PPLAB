st1=str(input("Enter String1:"))
st2=str(input("Enter String2:"))
if len(st1)==(st2):
    print("Strings with same length")
    for i in range(len(st1)):
        print(st1[i],end="")
    for i in range(len(st2)):
        print(st2[i],end="")
else:
    print("Strings with different length")
