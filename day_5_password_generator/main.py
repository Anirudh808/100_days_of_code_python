import random

# Define character sets
letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("0123456789")
symbols = list("!#$%&()*+")

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# **Easy Level (Ordered Password)**
password_list = random.choices(letters, k=nr_letters) + \
                random.choices(symbols, k=nr_symbols) + \
                random.choices(numbers, k=nr_numbers)

password_easy = "".join(password_list)
print(f"Easy Level Password: {password_easy}")

# **Hard Level (Shuffled Password)**
random.shuffle(password_list)
password_hard = "".join(password_list)
print(f"Hard Level Password: {password_hard}")
