empty ={} #Empty dictionary
marks = {
    "Rohit" : 100,
    "Mohit" : 80,
    "DR" : 200
}

#.item method give (keys,pairs) in Tuple form
print(marks.items())
#.keys will give you the keys mention in data
print(marks.keys())
# .update will update the dictionary it will make changes in Dictionary
# becoz it's muttable
marks.update({"Rohit" : 99, "Doctor" : 500})
# if key pairs doesn't exists then it gonna add it in dictionary like DOctor
print(marks)
# .get() method to get the value of key
print(marks.get("Rohit"))# if key doesn't exist it will give u NONE
print(marks["Rohit"]) #if key doesn't exist it will give u error
# Both work same but both are different

# len() is use to get the length of DIctionary
print(len(marks))