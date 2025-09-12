Exercise 1: Threaded Prime Number Checker

We’ll divide the range into chunks, assign each chunk to a thread, and check for primes in parallel.

import threading

# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Worker function for threads
def check_primes(start, end, result_list):
    local_primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            local_primes.append(num)
    result_list.extend(local_primes)

# Main program
if __name__ == "__main__":
    start_range = 1
    end_range = 100
    num_threads = 4

    # Split the range into chunks
    step = (end_range - start_range + 1) // num_threads
    threads = []
    primes = []

    for i in range(num_threads):
        sub_start = start_range + i * step
        # Last thread takes the rest
        sub_end = end_range if i == num_threads - 1 else (sub_start + step - 1)
        t = threading.Thread(target=check_primes, args=(sub_start, sub_end, primes))
        threads.append(t)
        t.start()

    # Wait for all threads
    for t in threads:
        t.join()

    primes.sort()
    print("Prime numbers:", primes)


🔹 This will output all prime numbers between 1 and 100, processed in parallel.

✅ Exercise 2: Threaded File Processing (Word Count)

We’ll split the file into chunks of lines, assign each chunk to a thread, count words locally, and merge results.

import threading
from collections import Counter

# Worker function for counting words
def count_words(lines, result_list):
    word_count = Counter()
    for line in lines:
        words = line.strip().split()
        word_count.update(words)
    result_list.append(word_count)

# Main program
if __name__ == "__main__":
    filename = "large_text.txt"  # replace with your file
    num_threads = 4

    # Read all lines
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Split lines among threads
    step = len(lines) // num_threads
    threads = []
    results = []

    for i in range(num_threads):
        start = i * step
        end = len(lines) if i == num_threads - 1 else (start + step)
        t = threading.Thread(target=count_words, args=(lines[start:end], results))
        threads.append(t)
        t.start()

    # Wait for all threads
    for t in threads:
        t.join()

    # Merge results
    final_count = Counter()
    for c in results:
        final_count.update(c)

    print("Word occurrences:")
    for word, count in final_count.most_common(10):  # top 10 words
        print(word, ":", count)
