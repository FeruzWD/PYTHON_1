Misollar:
# map() misol: Sonlarni kvadratlash
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, nums))
print("Squares:", squares)  # [1, 4, 9, 16, 25]

# filter() misol: Toq sonlarni olish
odds = list(filter(lambda x: x % 2 == 1, nums))
print("Odd numbers:", odds)  # [1, 3, 5]

1️⃣ is_prime(n) funksiyasi
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Test
print(is_prime(4))  # False
print(is_prime(7))  # True

2️⃣ digit_sum(k) funksiyasi
def digit_sum(k):
    return sum(int(d) for d in str(k))

# Test
print(digit_sum(24))   # 6  (2 + 4)
print(digit_sum(502))  # 7  (5 + 0 + 2)


👉 map() bilan ham yozish mumkin:

def digit_sum(k):
    return sum(map(int, str(k)))

3️⃣ Ikki sonning darajalari (2**k ≤ N)
def powers_of_two(N):
    k = 1
    while k <= N:
        print(k, end=" ")
        k *= 2

# Test
powers_of_two(10)  # 2 4 8


✅ Xullas:

map va filter qisqa funksiya yozishda juda qulay.

is_prime(n) → tub son tekshiradi.

digit_sum(k) → raqamlar yig‘indisi.

powers_of_two(N) → berilgan songacha bo‘lgan 2 ning darajalarini chiqaradi.

Xohlaysizmi, men sizga 3-masalani map() va filter() yordamida yozib ko‘rsatib beray?
