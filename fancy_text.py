# import pyfiglet module
from pyfiglet import figlet_format

# import fancify text module
from fancify_text import monospaced

# ask user to input name
name = input("Enter your name: ")

# ask user to input age
age = input("Enter your age: ")

# ask user to input their dream job
dream_job = input("What is your dream job?: ")

# add horizontal border 
print("=" * 100)

# print user's name in fancy way
print()
print(("----- Your name is ----- ").center(100))
print(figlet_format(name, font="univers", justify="center", width = 101))

# print the age in fancy age
print(monospaced("----- And your age is -----").center(100))
print(figlet_format(age, font="univers", justify="center", width = 101))

# print dream job in a fancy way
print(monospaced("----- and your dream job is to become a(n) -----").center(100))
print(figlet_format(dream_job, font="univers", justify="center", width = 101))

# print a short message in a fancy way
print()
print(("-" * 50).center(100))
print(monospaced("It won't be easy, but it'll be worth it :> ...").center(100))
print(("-" * 50).center(100))
print()

# add horizontal border 
print("=" * 100)
