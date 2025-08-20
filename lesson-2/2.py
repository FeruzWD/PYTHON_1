# 1. Age Calculator
name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))
current_year = 2025
age = current_year - birth_year
print(f"Hello {name}, you are {age} years old.")

# 2. Extract Car Names (txt = 'LMaasleitbtui')
txt = 'LMaasleitbtui'
car1 = txt[0] + txt[2] + txt[4] + txt[6] + txt[8]   # Lacet
car2 = txt[1] + txt[3] + txt[5] + txt[7] + txt[9] + txt[11]  # Malibu
print("Car names:", car1, car2)

# 3. Extract Car Names (txt = 'MsaatmiazD')
txt = 'MsaatmiazD'
car1 = txt[0] + txt[2] + txt[4] + txt[6] + txt[8]  # Matiz
car2 = txt[1] + txt[3] + txt[5] + txt[7] + txt[9]  # Damas
print("Car names:", car1, car2)

# 4. Extract Residence Area
txt = "I'am John. I am from London"
area = txt.split("from ")[1]
print("Residence area:", area)

# 5. Reverse String
s = input("Enter a string: ")
print("Reversed string:", s[::-1])

# 6. Count Vowels
s = input("Enter a string to count vowels: ")
vowels = "aeiouAEIOU"
count = sum(1 for ch in s if ch in vowels)
print("Number of vowels:", count)

# 7. Find Maximum Value
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Maximum value:", max(numbers))

# 8. Check Palindrome
word = input("Enter a word: ")
if word == word[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")

# 9. Extract Email Domain
email = input("Enter your email: ")
domain = email.split("@")[1]
print("Email domain:", domain)

# 10. Generate Random Password
import random, string
length = 12
characters = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.choice(characters) for i in range(length))
print("Generated password:", password)
