#1 
txt = "MsaatmiazD"
txt[::2]
#2
country = "I'm John. I am from London"
country.split()[-1]
#3
maksimaka = input("Matnni kiriting")
maksimaka[::-1]
#4
mevalar = ["Olma", "Anor", "Gilos", "Nok", "Uzum"]
print("Uchinchi meva:", mevalar[2])
#5
royxat = [10, 20, 30, 40, 50]
yangi = [royxat[0], royxat[len(royxat)//2], royxat[-1]]
print("Yangi ro‘yxat:", yangi)
#6
sonlar = [1, 2, 3]
takrorlangan = sonlar * 2
print("Takrorlangan ro‘yxat:", takrorlangan)
#7
numbers = [10, 20, 30, 40]
numbers[0], numbers[-1] = numbers[-1], numbers[0]
print("Almashtirilgan ro‘yxat:", numbers)
