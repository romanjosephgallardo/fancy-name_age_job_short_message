from pyfiglet import figlet_format

# pseudocode


# ask user to input name
name = input("Enter your name: ")

# ask user to input age
age = input("Enter your age: ")

# ask user to input their dream job
dream_job = input("What is your dream job?: ")


# add horizontal border 
print("=" * 100)
# print user's name in fancy way
print(figlet_format(name, font="univers"))

# print the age in fancy age
print(figlet_format(age, font="univers"))

# print dream job in a fancy way
print(figlet_format(dream_job, font="univers"))

# provide a short message

# add horizontal border 
print("=" * 100)
