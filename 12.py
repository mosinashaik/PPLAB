str=input('Enter a string ')
str_split=str.split(' ')
str_join='-'.join(str_split)
str_dec={idx:ele for idx,ele in enumerate(str_split)}
print('Dictionary after spliting')
print(str_dec)
print('String after join with ''-'' ')
print(str_join)
