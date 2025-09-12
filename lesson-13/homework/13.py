1. Age Calculator
from datetime import date, datetime

birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()
today = date.today()

years = today.year - birthdate.year
months = today.month - birthdate.month
days = today.day - birthdate.day

if days < 0:
    months -= 1
    days += (date(today.year, today.month, 1) - date(today.year, today.month - 1, 1)).days
if months < 0:
    years -= 1
    months += 12

print(f"You are {years} years, {months} months, and {days} days old.")

✅ 2. Days Until Next Birthday
from datetime import date, datetime, timedelta

birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()
today = date.today()

next_birthday = date(today.year, birthdate.month, birthdate.day)
if next_birthday < today:
    next_birthday = date(today.year + 1, birthdate.month, birthdate.day)

days_remaining = (next_birthday - today).days
print(f"Your next birthday is in {days_remaining} days.")

✅ 3. Meeting Scheduler
from datetime import datetime, timedelta

current_str = input("Enter current date and time (YYYY-MM-DD HH:MM): ")
duration_str = input("Enter meeting duration (hours minutes): ")

current_time = datetime.strptime(current_str, "%Y-%m-%d %H:%M")
hours, minutes = map(int, duration_str.split())

end_time = current_time + timedelta(hours=hours, minutes=minutes)
print("Meeting will end at:", end_time.strftime("%Y-%m-%d %H:%M"))

✅ 4. Timezone Converter
from datetime import datetime
import pytz

dt_str = input("Enter date and time (YYYY-MM-DD HH:MM): ")
src_tz_str = input("Enter your timezone (e.g., Asia/Tashkent): ")
dst_tz_str = input("Enter target timezone (e.g., Europe/London): ")

dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M")
src_tz = pytz.timezone(src_tz_str)
dst_tz = pytz.timezone(dst_tz_str)

localized_dt = src_tz.localize(dt)
converted_dt = localized_dt.astimezone(dst_tz)

print("Converted time:", converted_dt.strftime("%Y-%m-%d %H:%M"))

✅ 5. Countdown Timer
from datetime import datetime
import time

future_str = input("Enter future date and time (YYYY-MM-DD HH:MM:SS): ")
future_time = datetime.strptime(future_str, "%Y-%m-%d %H:%M:%S")

while True:
    now = datetime.now()
    remaining = future_time - now
    if remaining.total_seconds() <= 0:
        print("Time's up!")
        break
    print("Time remaining:", remaining)
    time.sleep(1)

✅ 6. Email Validator
import re

email = input("Enter your email: ")
pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

if re.match(pattern, email):
    print("Valid email address ✅")
else:
    print("Invalid email ❌")

✅ 7. Phone Number Formatter
phone = input("Enter phone number (digits only): ")

if len(phone) == 10 and phone.isdigit():
    formatted = f"({phone[:3]}) {phone[3:6]}-{phone[6:]}"
    print("Formatted:", formatted)
else:
    print("Invalid phone number")

✅ 8. Password Strength Checker
import re

password = input("Enter a password: ")

if (len(password) >= 8 and
    re.search(r"[A-Z]", password) and
    re.search(r"[a-z]", password) and
    re.search(r"[0-9]", password)):
    print("Strong password 💪")
else:
    print("Weak password ❌ (must contain upper, lower, digit, min 8 chars)")

✅ 9. Word Finder
text = "Python is fun. Python is powerful. I love Python programming."
word = input("Enter word to find: ")

positions = []
start = 0
while True:
    index = text.lower().find(word.lower(), start)
    if index == -1:
        break
    positions.append(index)
    start = index + len(word)

if positions:
    print(f"Word '{word}' found at positions: {positions}")
else:
    print(f"Word '{word}' not found.")

✅ 10. Date Extractor
import re

text = input("Enter a text with dates: ")

# Matches YYYY-MM-DD or DD/MM/YYYY formats
pattern = r'(\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4})'
dates = re.findall(pattern, text)

if dates:
    print("Dates found:", dates)
else:
    print("No dates found")
