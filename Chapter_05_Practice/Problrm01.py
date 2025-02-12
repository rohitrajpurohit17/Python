# Write a program to create a dictionary of Hindi words with values as their English 
# translation. Provide user with an option to look it up! 

dict = {
    "madad" : "Help",
    "Kursi" : "chair",
    "Billi" : "Cat"
}

word = input("Enter the word you want : ")
print(dict[word])
# It will give Error if the word doesn't exists in dictonary
# It is Case Sensetive A-a are differet