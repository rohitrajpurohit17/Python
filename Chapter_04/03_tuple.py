# Tuples are just like list but Tuple is immutable ... it can't be change
a =() 
#it is empty tuple
print(type(a))
b =(4) 
#it is int type data type , it's not tuple
print(type(b))
c =(4,) 
#To make that integre to tuple we have to put , coma after the data
print(type(c))
d =(4,"Rohit","DR",21.20) 
#Like mention before just like List
print(type(d))
print(d)
# It's for to count how many times it repeated
r = d.count(4)
print(r)
# index is for to check in which index particular element is present 
# if i get element it will stop searching doesn't matter same element present multiple time
# it stop at the point it found 
f = d.index(4)
print(f)