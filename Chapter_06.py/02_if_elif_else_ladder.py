# if elif else ladder
age = int(input("Enter age: "))

if(age >= 18):
    print("You are eligibale")

elif(age <= 0):
    print("Invalid age")

elif(age < 18 and age > 0):
    print("You are Small")

else:
    print("Wrong Input")