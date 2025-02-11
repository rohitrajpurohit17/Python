#  Sets are unordered => Element’s order doesn’t matter 
#  Sets are unindexed => Cannot access elements by index 
#  There is no way to change items in sets. 
#  Sets cannot contain duplicate values. 

e = set() # use to create empty set
print(type(e))
# Don't use e = {} because it wil create an empty Dictionary

# In set element can't be repeat as shown below
s = {1,10,50,2,2,1}
print(s)
# Set will not maintain order for that u have to use LIST