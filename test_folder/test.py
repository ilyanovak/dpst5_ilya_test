from pandas import DataFrame


print("HELLO!")

df = DataFrame({'a':[1,2,3], 'b':[4,5,6]})

print(df.head)

from test_folder.my_mod import enlarge

x=11
print(enlarge(x))