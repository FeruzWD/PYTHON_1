. Exception Handling Exercises
# 1. Handle ZeroDivisionError
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# 2. Handle ValueError for invalid integer
try:
    n = int(input("Enter an integer: "))
except ValueError:
    print("Error: That was not a valid integer.")

# 3. Handle FileNotFoundError
try:
    with open("nonexistent.txt") as f:
        content = f.read()
except FileNotFoundError:
    print("Error: File not found.")

# 4. Handle TypeError for non-numerical inputs
try:
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    if not (a.isdigit() and b.isdigit()):
        raise TypeError("Inputs must be numbers")
    print(int(a) + int(b))
except TypeError as e:
    print("Error:", e)

# 5. Handle PermissionError
try:
    with open("/root/secret.txt") as f:  # no permission
        print(f.read())
except PermissionError:
    print("Error: You do not have permission to open this file.")

# 6. Handle IndexError
try:
    lst = [1, 2, 3]
    print(lst[5])
except IndexError:
    print("Error: List index out of range.")

# 7. Handle KeyboardInterrupt
try:
    n = input("Enter a number (Ctrl+C to cancel): ")
except KeyboardInterrupt:
    print("\nInput cancelled by user.")

# 8. Handle ArithmeticError
try:
    x = 10 / 0
except ArithmeticError:
    print("Arithmetic error occurred.")

# 9. Handle UnicodeDecodeError
try:
    with open("file.txt", encoding="ascii") as f:
        print(f.read())
except UnicodeDecodeError:
    print("Error: Encoding issue while reading file.")

# 10. Handle AttributeError
try:
    lst = [1, 2, 3]
    lst.push(4)  # wrong method
except AttributeError:
    print("Error: List has no such attribute.")

📘 2. File Input/Output Exercises
# 1. Read entire file
with open("sample.txt") as f:
    print(f.read())

# 2. Read first n lines
n = 3
with open("sample.txt") as f:
    for i in range(n):
        print(f.readline().strip())

# 3. Append text to file
with open("sample.txt", "a") as f:
    f.write("\nAppended line.")
with open("sample.txt") as f:
    print(f.read())

# 4. Read last n lines
n = 2
with open("sample.txt") as f:
    lines = f.readlines()
    print("".join(lines[-n:]))

# 5. Read file line by line into a list
with open("sample.txt") as f:
    lines = f.readlines()
print(lines)

# 6. Read file into a variable
with open("sample.txt") as f:
    data = f.read()
print(data)

# 7. Read file into an array
import array
with open("sample.txt") as f:
    arr = [line.strip() for line in f]
print(arr)

# 8. Find longest words
with open("sample.txt") as f:
    words = f.read().split()
longest = max(words, key=len)
print("Longest word:", longest)

# 9. Count number of lines
with open("sample.txt") as f:
    print("Number of lines:", len(f.readlines()))

# 10. Word frequency
from collections import Counter
with open("sample.txt") as f:
    words = f.read().replace(",", " ").split()
print(Counter(words))

# 11. File size
import os
print("File size:", os.path.getsize("sample.txt"), "bytes")

# 12. Write a list to file
my_list = ["apple", "banana", "cherry"]
with open("list.txt", "w") as f:
    f.writelines("\n".join(my_list))

# 13. Copy file contents
with open("sample.txt") as f, open("copy.txt", "w") as out:
    out.write(f.read())

# 14. Combine lines from two files
with open("file1.txt") as f1, open("file2.txt") as f2:
    for l1, l2 in zip(f1, f2):
        print(l1.strip() + " " + l2.strip())

# 15. Read a random line
import random
with open("sample.txt") as f:
    lines = f.readlines()
print("Random line:", random.choice(lines))

# 16. Check if file is closed
f = open("sample.txt")
print("File closed?", f.closed)
f.close()
print("File closed?", f.closed)

# 17. Remove newline characters
with open("sample.txt") as f:
    clean = [line.strip() for line in f]
print(clean)

# 18. Count words in a file
with open("sample.txt") as f:
    text = f.read().replace(",", " ")
    print("Word count:", len(text.split()))

# 19. Extract characters from multiple files
import glob
chars = []
for filename in glob.glob("*.txt"):
    with open(filename) as f:
        chars.extend(list(f.read()))
print(chars)

# 20. Generate 26 text files A-Z
import string
for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w") as f:
        f.write(f"This is file {letter}\n")

# 21. Alphabet file with specified number per line
letters = string.ascii_uppercase
n = 5  # letters per line
with open("alphabet.txt", "w") as f:
    for i in range(0, len(letters), n):
        f.write("".join(letters[i:i+n]) + "\n")
