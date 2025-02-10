#This program is about Dictionary
# 1. It is unordered. 
# 2. It is mutable. 
# 3. It is indexed. 
# 4. Cannot contain duplicate keys. 
marks = {
    "Rohit" : 100,
    "Mohit" : 80,
    "DR" : 200, #Duplicates are not allowed example
    "DR" : 100
}
# It is same like list and tuple

print(marks,"\n", type(marks))
print(marks["Rohit"])