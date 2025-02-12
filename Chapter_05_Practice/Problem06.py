# Create an empty dictionary. Allow 4 friends to enter their favorite language as 
# value and use key as their names. Assume that the names are unique. 
fav = {

}
name = input("Enter Name : ")
sub = input("Enter favourit Sunject :")
fav.update({name:sub})
name = input("Enter Name : ")
sub = input("Enter favourit Sunject :")
fav.update({name:sub})
name = input("Enter Name : ")
sub = input("Enter favourit Sunject :")
fav.update({name:sub})

print(fav)