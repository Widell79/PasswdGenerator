#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_chars= input("Enter the number of Letters, Symbols and Numbers requested in password. e.g. '422'\n") 
nr_letters = int(nr_chars[0])
nr_symbols = int(nr_chars[1])
nr_numbers = int(nr_chars[2])

password = []

for letter in range(1, nr_letters +1):
  password.append(random.choice(letters))

for symbol in range(1, nr_symbols +1):
  password.append(random.choice(symbols))

for number in range(1, nr_numbers +1):
  password.append(random.choice(numbers))

random.shuffle(password)
passwd_string = "".join(password)
 
print(f"Your generated password: {passwd_string}")