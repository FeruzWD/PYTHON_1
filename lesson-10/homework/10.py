from datetime import datetime

class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "✅ Done" if self.completed else "❌ Not Done"
        return f"{self.title} | {self.description} | Due: {self.due_date.date()} | {status}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_all_tasks(self):
        for t in self.tasks:
            print(t)

    def incomplete_tasks(self):
        for t in self.tasks:
            if not t.completed:
                print(t)


# === Main Program ===
def main():
    todo = ToDoList()
    while True:
        print("\nToDo Menu: 1.Add Task 2.Mark Complete 3.List All 4.Incomplete 5.Exit")
        choice = input("Choose: ")

        if choice == "1":
            title = input("Task title: ")
            desc = input("Description: ")
            due = input("Due date (YYYY-MM-DD): ")
            task = Task(title, desc, due)
            todo.add_task(task)

        elif choice == "2":
            todo.list_all_tasks()
            index = int(input("Task number to mark complete: ")) - 1
            if 0 <= index < len(todo.tasks):
                todo.tasks[index].mark_complete()

        elif choice == "3":
            todo.list_all_tasks()

        elif choice == "4":
            todo.incomplete_tasks()

        elif choice == "5":
            break

if __name__ == "__main__":
    main()
📰 Homework 2: Simple Blog System
python
Копировать
Редактировать
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}\n{self.content}\n"

class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_posts(self):
        for p in self.posts:
            print(p)

    def posts_by_author(self, author):
        for p in self.posts:
            if p.author == author:
                print(p)

    def delete_post(self, title):
        self.posts = [p for p in self.posts if p.title != title]

    def edit_post(self, old_title, new_title, new_content):
        for p in self.posts:
            if p.title == old_title:
                p.title = new_title
                p.content = new_content

    def latest_posts(self, n=3):
        for p in self.posts[-n:]:
            print(p)


# === Main Program ===
def main():
    blog = Blog()
    while True:
        print("\nBlog Menu: 1.Add 2.List 3.By Author 4.Delete 5.Edit 6.Latest 7.Exit")
        choice = input("Choose: ")

        if choice == "1":
            title = input("Title: ")
            content = input("Content: ")
            author = input("Author: ")
            blog.add_post(Post(title, content, author))

        elif choice == "2":
            blog.list_posts()

        elif choice == "3":
            author = input("Author: ")
            blog.posts_by_author(author)

        elif choice == "4":
            title = input("Title to delete: ")
            blog.delete_post(title)

        elif choice == "5":
            old_title = input("Old title: ")
            new_title = input("New title: ")
            new_content = input("New content: ")
            blog.edit_post(old_title, new_title, new_content)

        elif choice == "6":
            blog.latest_posts()

        elif choice == "7":
            break

if __name__ == "__main__":
    main()
💰 Homework 3: Simple Banking System
python
Копировать
Редактировать
class Account:
    def __init__(self, acc_number, holder, balance=0):
        self.acc_number = acc_number
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("❌ Insufficient funds!")
        else:
            self.balance -= amount

    def __str__(self):
        return f"Account {self.acc_number} | {self.holder} | Balance: {self.balance}"

class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, acc):
        self.accounts[acc.acc_number] = acc

    def get_account(self, acc_number):
        return self.accounts.get(acc_number, None)

    def transfer(self, from_acc, to_acc, amount):
        if from_acc in self.accounts and to_acc in self.accounts:
            if self.accounts[from_acc].balance >= amount:
                self.accounts[from_acc].withdraw(amount)
                self.accounts[to_acc].deposit(amount)
            else:
                print("❌ Not enough balance to transfer.")


# === Main Program ===
def main():
    bank = Bank()
    while True:
        print("\nBank Menu: 1.Add Account 2.Check Balance 3.Deposit 4.Withdraw 5.Transfer 6.All Accounts 7.Exit")
        choice = input("Choose: ")

        if choice == "1":
            num = input("Account number: ")
            name = input("Holder name: ")
            bal = float(input("Initial balance: "))
            bank.add_account(Account(num, name, bal))

        elif choice == "2":
            num = input("Account number: ")
            acc = bank.get_account(num)
            if acc: print(acc)
            else: print("Account not found")

        elif choice == "3":
            num = input("Account number: ")
            acc = bank.get_account(num)
            if acc:
                amt = float(input("Deposit amount: "))
                acc.deposit(amt)

        elif choice == "4":
            num = input("Account number: ")
            acc = bank.get_account(num)
            if acc:
                amt = float(input("Withdraw amount: "))
                acc.withdraw(amt)

        elif choice == "5":
            from_acc = input("From account: ")
            to_acc = input("To account: ")
            amt = float(input("Transfer amount: "))
            bank.transfer(from_acc, to_acc, amt)

        elif choice == "6":
            for acc in bank.accounts.values():
                print(acc)

        elif choice == "7":
            break

if __name__ == "__main__":
    main()
