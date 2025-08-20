# 1. Create and Access List Elements
fruits = ["apple", "banana", "mango", "orange", "grape"]
print("Third fruit:", fruits[2])

# 2. Concatenate Two Lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated = list1 + list2
print("Concatenated list:", concatenated)

# 3. Extract Elements from a List
numbers = [10, 20, 30, 40, 50]
first = numbers[0]
middle = numbers[len(numbers)//2]
last = numbers[-1]
new_list = [first, middle, last]
print("New list:", new_list)

# 4. Convert List to Tuple
movies = ["Inception", "Titanic", "Avatar", "Matrix", "Gladiator"]
movies_tuple = tuple(movies)
print("Movies tuple:", movies_tuple)

# 5. Check Element in a List
cities = ["London", "Paris", "New York", "Berlin"]
print("Is Paris in the list?", "Paris" in cities)

# 6. Duplicate a List Without Using Loops
nums = [1, 2, 3]
duplicated = nums * 2
print("Duplicated list:", duplicated)

# 7. Swap First and Last Elements of a List
nums = [10, 20, 30, 40]
nums[0], nums[-1] = nums[-1], nums[0]
print("Swapped list:", nums)

# 8. Slice a Tuple
t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("Slice 3 to 7:", t[3:8])

# 9. Count Occurrences in a List
colors = ["red", "blue", "green", "blue", "yellow", "blue"]
print("Blue appears:", colors.count("blue"), "times")

# 10. Find the Index of an Element in a Tuple
animals = ("tiger", "lion", "elephant", "zebra")
print("Index of lion:", animals.index("lion"))

# 11. Merge Two Tuples
t1 = (1, 2, 3)
t2 = (4, 5, 6)
merged = t1 + t2
print("Merged tuple:", merged)

# 12. Find the Length of a List and Tuple
my_list = [1, 2, 3, 4]
my_tuple = (10, 20, 30)
print("Length of list:", len(my_list))
print("Length of tuple:", len(my_tuple))

# 13. Convert Tuple to List
nums_tuple = (11, 22, 33, 44, 55)
nums_list = list(nums_tuple)
print("Converted list:", nums_list)

# 14. Find Maximum and Minimum in a Tuple
numbers = (15, 2, 78, 34, 6)
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))

# 15. Reverse a Tuple
words = ("python", "java", "c++", "ruby")
print("Reversed tuple:", words[::-1])
