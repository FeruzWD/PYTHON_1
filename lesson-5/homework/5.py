Leap Year Function

Your function just needed small formatting fixes. Here’s the correct version:

def is_leap(year):
    """
    Determines whether a given year is a leap year.

    A year is a leap year if:
    - It is divisible by 4, and
    - It is NOT divisible by 100, unless it is also divisible by 400.

    Parameters:
        year (int): The year to be checked.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    """
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


# Example
print(is_leap(2000))  # True
print(is_leap(1900))  # False
print(is_leap(2024))  # True

✅ 2. Conditional Statements Exercise

This matches the HackerRank "Weird or Not Weird" problem.

def check_number(n):
    if n % 2 == 1:
        print("Weird")
    elif n % 2 == 0 and 2 <= n <= 5:
        print("Not Weird")
    elif n % 2 == 0 and 6 <= n <= 20:
        print("Weird")
    elif n % 2 == 0 and n > 20:
        print("Not Weird")

# Example
check_number(3)   # Weird
check_number(4)   # Not Weird
check_number(18)  # Weird
check_number(22)  # Not Weird

✅ 3. Even Numbers Between a and b (inclusive) Without Loop
🔹 Solution 1: Using if-else (check whether a is even or odd)
def evens_between_ifelse(a, b):
    # Make sure a is even
    if a % 2 != 0:
        a += 1
    # Use range() and list() directly (no explicit loop)
    return list(range(a, b+1, 2))

# Example
print(evens_between_ifelse(3, 10))  # [4, 6, 8, 10]
print(evens_between_ifelse(2, 9))   # [2, 4, 6, 8]

🔹 Solution 2: Without if-else (use math trick)
def evens_between_no_if(a, b):
    # Start from the first even number >= a
    start = a + (a % 2)
    return list(range(start, b+1, 2))

# Example
print(evens_between_no_if(3, 10))  # [4, 6, 8, 10]
print(evens_between_no_if(2, 9))   # [2, 4, 6, 8]


✅ Summary:

is_leap(year) → returns True/False for leap years.

check_number(n) → prints "Weird" or "Not Weird".

Two ways to get evens between a and b without loop.
