1. Circle Class
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


# Example
c = Circle(5)
print("Circle Area:", c.area())
print("Circle Perimeter:", c.perimeter())

📘 2. Person Class
from datetime import date, datetime

class Person:
    def __init__(self, name, country, dob):  # dob = "YYYY-MM-DD"
        self.name = name
        self.country = country
        self.dob = datetime.strptime(dob, "%Y-%m-%d").date()

    def age(self):
        today = date.today()
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))


# Example
p = Person("Ali", "Uzbekistan", "2000-05-10")
print(p.name, "Age:", p.age())

📘 3. Calculator Class
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b


# Example
calc = Calculator()
print("5 + 3 =", calc.add(5, 3))
print("10 / 0 =", calc.divide(10, 0))

📘 4. Shape and Subclasses
import math

class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2
    def perimeter(self):
        return 4 * self.side

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c
    def perimeter(self):
        return self.a + self.b + self.c
    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


# Example
sq = Square(4)
print("Square Area:", sq.area())

📘 5. Binary Search Tree
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if key < root.key:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert(root.left, key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert(root.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.key == key:
            return root is not None
        if key < root.key:
            return self._search(root.left, key)
        return self._search(root.right, key)


# Example
bst = BST()
for x in [10, 5, 15, 3, 7]:
    bst.insert(x)
print("Search 7:", bst.search(7))

📘 6. Stack Class
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.stack:
            return "Stack is empty"
        return self.stack.pop()


# Example
s = Stack()
s.push(10)
print(s.pop())

📘 7. Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp:
            prev.next = temp.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# Example
ll = LinkedList()
ll.insert(3)
ll.insert(2)
ll.insert(1)
ll.display()
ll.delete(2)
ll.display()

📘 8. Shopping Cart
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, price):
        self.items[item] = self.items.get(item, 0) + price

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]

    def total(self):
        return sum(self.items.values())


# Example
cart = ShoppingCart()
cart.add_item("Apple", 3)
cart.add_item("Banana", 2)
print("Total:", cart.total())

📘 9. Stack with Display
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.stack:
            return "Stack is empty"
        return self.stack.pop()

    def display(self):
        print("Stack:", self.stack)


# Example
s = Stack()
s.push(5)
s.push(10)
s.display()

📘 10. Queue Class
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.queue:
            return "Queue is empty"
        return self.queue.pop(0)


# Example
q = Queue()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())

📘 11. Bank Class
class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount

    def __str__(self):
        return f"{self.name}: {self.balance} USD"

class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, name, balance=0):
        self.accounts[name] = BankAccount(name, balance)

    def get_account(self, name):
        return self.accounts.get(name, None)


# Example
bank = Bank()
bank.add_account("Ali", 100)
acc = bank.get_account("Ali")
acc.deposit(50)
print(acc)
