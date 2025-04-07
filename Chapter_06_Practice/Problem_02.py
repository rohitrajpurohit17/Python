marks1 = int(input("Enetr marks1: "))
marks2 = int(input("Enetr marks2: "))
marks3 = int(input("Enetr marks3: "))

total_percentage = (marks1+marks2+marks3)/3

if(total_percentage > 40 and marks1 > 33 and marks2 > 33 and marks3 > 33):
    print("You passed congratulation:",total_percentage)
else:
    print("You failed:",total_percentage)