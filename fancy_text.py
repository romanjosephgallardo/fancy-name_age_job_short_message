from pyfiglet import figlet_format
from fancify_text import monospaced
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
print(("----- Your name is ----- ").center(100))
print(figlet_format(name, font="univers", justify="center", width = 100))

# print the age in fancy age
print(("----- And your age is -----").center(100))
print(figlet_format(age, font="univers", justify="center", width = 100))

# print dream job in a fancy way
print(("----- and our dream job is to become a(n) -----").center(100))
print(figlet_format(dream_job, font="univers", justify="center", width = 100))

# provide a short message

# add horizontal border 
print("=" * 100)
