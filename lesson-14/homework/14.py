Task 1: JSON Parsing (students.json)
import json

# students.json sample:
# [
#   {"name": "Ali", "age": 20, "major": "CS"},
#   {"name": "Laylo", "age": 21, "major": "Math"}
# ]

with open("students.json", "r", encoding="utf-8") as f:
    students = json.load(f)

print("Student Details:")
for s in students:
    print(f"Name: {s['name']}, Age: {s['age']}, Major: {s['major']}")

✅ Task 2: Weather API (OpenWeatherMap)

👉 Sign up at OpenWeatherMap
 and get a free API key.

import requests

API_KEY = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
CITY = "Tashkent"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
if response.status_code == 200:
    data = response.json()
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather = data["weather"][0]["description"]

    print(f"Weather in {CITY}:")
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {weather}")
else:
    print("Error fetching weather data:", response.status_code)

✅ Task 3: JSON Modification (books.json)

We’ll allow add, update, delete from books.json.

import json
import os

FILE = "books.json"

# Ensure file exists
if not os.path.exists(FILE):
    with open(FILE, "w") as f:
        json.dump([], f)

def load_books():
    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_books(books):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(books, f, indent=4)

def add_book(title, author):
    books = load_books()
    books.append({"title": title, "author": author})
    save_books(books)
    print("Book added ✅")

def update_book(old_title, new_title, new_author):
    books = load_books()
    for b in books:
        if b["title"].lower() == old_title.lower():
            b["title"], b["author"] = new_title, new_author
            save_books(books)
            print("Book updated ✅")
            return
    print("Book not found ❌")

def delete_book(title):
    books = load_books()
    books = [b for b in books if b["title"].lower() != title.lower()]
    save_books(books)
    print("Book deleted ✅")

# Example usage
add_book("1984", "George Orwell")
update_book("1984", "Nineteen Eighty-Four", "George Orwell")
delete_book("Nineteen Eighty-Four")

✅ Task 4: Movie Recommendation System (OMDb API)

👉 Get a free API key from OMDb API
.

import requests
import random

API_KEY = "YOUR_OMDB_API_KEY"  # Replace with your OMDb API key

def recommend_movie(genre):
    url = f"http://www.omdbapi.com/?apikey={API_KEY}&s={genre}&type=movie"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if "Search" in data:
            movies = data["Search"]
            choice = random.choice(movies)
            print("Movie Recommendation 🎬")
            print(f"Title: {choice['Title']}")
            print(f"Year: {choice['Year']}")
            print(f"IMDB ID: {choice['imdbID']}")
        else:
            print("No movies found for that genre ❌")
    else:
        print("Error fetching data:", response.status_code)

# Example usage
genre = input("Enter movie genre (e.g., Action, Comedy, Drama): ")
recommend_movie(genre)
