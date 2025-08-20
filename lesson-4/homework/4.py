# 1. Sort a Dictionary by Value
d = {2: 30, 1: 10, 3: 20}
asc = dict(sorted(d.items(), key=lambda x: x[1]))
desc = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
print("Ascending:", asc)
print("Descending:", desc)

# 2. Add a Key to a Dictionary
d = {0: 10, 1: 20}
d[2] = 30
print("Updated dictionary:", d)

# 3. Concatenate Multiple Dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
new_dic = {}
for dic in (dic1, dic2, dic3):
    new_dic.update(dic)
print("Concatenated dictionary:", new_dic)

# 4. Generate a Dictionary with Squares
n = 5
squares = {x: x*x for x in range(1, n+1)}
print("Squares dictionary:", squares)

# 5. Dictionary of Squares (1 to 15)
squares_15 = {x: x*x for x in range(1, 16)}
print("Squares 1–15:", squares_15)
📘 Set Exercises
python
Копировать
Редактировать
# 1. Create a Set
my_set = {1, 2, 3, 4}
print("Created set:", my_set)

# 2. Iterate Over a Set
for item in my_set:
    print("Set item:", item)

# 3. Add Member(s) to a Set
my_set.add(5)
my_set.update([6, 7])
print("After adding members:", my_set)

# 4. Remove Item(s) from a Set
my_set.remove(7)   # will give error if element not found
print("After removing 7:", my_set)

# 5. Remove an Item if Present in the Set
my_set.discard(10)   # no error even if 10 not present
print("After discarding 10 (if present):", my_set)
