# in this first program we are taking input but it comes as string 
# if we add strings they joins
a = input("Enter number 1: ")

b = input("Enter number 2: ")
# if a = 5 & b = 5 , it will give sum 55 becooz strings joins
print("Number a is: ", a)
print("Number b is: ", b) 
print("Sum is ", a + b)

# To avoid that we have to convert that input in required data type
x = int(input("Enter number 1: "))

y = int(input("Enter number 2: "))

print("Number a is: ", x)
print("Number b is: ", y) 
print("Sum is ", x + y)