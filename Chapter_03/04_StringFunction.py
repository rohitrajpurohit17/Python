# name = "Rajpurohit"
# print(len(name))
# print(name.endswith("hit"))
# Above are done by me for my understanding
# Below is done with help of AI as mention before better understaing about AI in programming

# Example string
string = "Rajpurohit"

# 1. len(): Gets the length of the string
length = len(string)
print(f"Length of string: {length}")

# 2. lower(): Converts the string to lower case
lowercase = string.lower()
print(f"Lowercase string: {lowercase}")

# 3. upper(): Converts the string to upper case
uppercase = string.upper()
print(f"Uppercase string: {uppercase}")

# 4. replace(): Replaces a substring with another substring
replaced = string.replace("Raj", "Rajesh")
print(f"Replaced string: {replaced}")

# 5. find(): Finds the position of a substring
position = string.find("purohit")
print(f"Position of 'purohit': {position}")

# 6. split(): Splits the string into a list using the specified delimiter
split_string = string.split("purohit")
print(f"Split string: {split_string}")

# 7. join(): Joins a list of strings into a single string, using a specified delimiter
joined_string = "-".join(split_string)
print(f"Joined string: {joined_string}")

# 8. strip(): Removes leading and trailing whitespace
whitespace_string = " Rajpurohit "
stripped_string = whitespace_string.strip()
print(f"Stripped string: '{stripped_string}'")

# 9. isalpha(): Checks if the string contains only alphabetic characters
is_alpha = string.isalpha()
print(f"Is string alphabetic: {is_alpha}")

# 10. startswith(): Checks if the string starts with a specific substring
starts_with = string.startswith("Raj")
print(f"Starts with 'Raj': {starts_with}")

# 11. endswith(): Checks if the string ends with a specific substring
ends_with = string.endswith("purohit")
print(f"Ends with 'purohit': {ends_with}")
