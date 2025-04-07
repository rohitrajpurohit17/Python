a = int(input("Enter Num1: "))
b = int(input("Enter Num2: "))
c = int(input("Enter Num3: "))
d = int(input("Enter Num4: "))

if(a > b and a > c and a >d):
    print("a is greater:",a)

elif(b > a and b > c and b > d):
    print("b is greater:",b)

elif(c > a and c > b and c > d):
    print("c is greater:",c)
else:
    print("d is greater:",d)