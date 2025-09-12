import sqlite3

# Connect (creates new DB file if not exists)
conn = sqlite3.connect("star_trek.db")
cursor = conn.cursor()

# 1. Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
""")

# 2. Insert values
data = [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
]
cursor.executemany("INSERT INTO Roster VALUES (?, ?, ?)", data)

# 3. Update Jadzia Dax -> Ezri Dax
cursor.execute("""
UPDATE Roster
SET Name = 'Ezri Dax'
WHERE Name = 'Jadzia Dax'
""")

# 4. Select Bajorans
cursor.execute("""
SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'
""")
results = cursor.fetchall()

print("Bajoran crew members:")
for name, age in results:
    print(f"{name} (Age {age})")

# Save & close
conn.commit()
conn.close()
