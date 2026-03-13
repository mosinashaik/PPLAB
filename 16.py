def first_diff(s1, s2):
    if len(s1) == len(s2):
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                return i
        return -1   # if strings are equal
    else:
        return -1

s1 = input('Enter first String: ')
s2 = input('Enter second String: ')
result = first_diff(s1, s2)

print('The desired result:', result)
