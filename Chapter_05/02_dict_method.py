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
marks.update({"Rohit" : 99})
print(marks)