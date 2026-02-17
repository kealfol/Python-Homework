import math

print("\nЗадание № 1")
film = input("Введите название фильма: ")
cinema = input("Введите название кинотеатра: ")
time = input("Введите время: ")
print(f'Билет на "{film}" в "{cinema}" на {time} забронирован.')


print("\nЗадание № 2")
str1 = input("Введите первую строку: ")
str2 = input("Введите вторую строку: ")
if (str1 == "да" or str1 == "нет") and (str2 == "да" or str2 == "нет"):
    print("ВЕРНО")
else:
    print("НЕВЕРНО")


print("\nЗадание № 3")
login = input("Введите логин: ")
email = input("Введите резервный адрес: ")
if "@" not in login and "@" in email:
    print("OK")
else:
    print("Некорректный логин или адрес")


print("\nЗадание № 4")
print(input())


print("\nЗадание № 5")
string = input("Введите строку: ")
if string == "":
    print("ДА")
else:
    print("НЕТ")


print("\nЗадание № 6")
number = int(input("Введите трехзначное число: "))
d1 = number // 100
d2 = number // 10 % 10
d3 = number % 10
max_d = max(d1, d2, d3)
min_d = min(d1, d2, d3)
mid_d = (d1 + d2 + d3) - max_d - min_d
if (max_d + min_d) / 2 == mid_d:
    print("Вы ввели красивое число")
else:
    print("Жаль, вы ввели обычное число")


print("\nЗадание № 7")
num = int(input("Введите 4-х значное число: "))
a = num // 1000
b = num // 100 % 10
c = num // 10 % 10
d = num % 10
if a > b: a, b = b, a
if b > c: b, c = c, b
if c > d: c, d = d, c
if a > b: a, b = b, a
if b > c: b, c = c, b
if a > b: a, b = b, a
if a == 0:
    if b != 0: a, b = b, a
    elif c != 0: a, c = c, a
    else: a, d = d, a
print(a * 1000 + b * 100 + c * 10 + d)


print("\nЗадание № 8")
count = 0
min_h = 200
max_h = 0
print("Введите рост (для завершения - !):")
while True:
    h_in = input()
    if h_in == "!":
        break
    h = int(h_in)
    if 150 <= h <= 190:
        count += 1
        if h < min_h: min_h = h
        if h > max_h: max_h = h
print(count)
if count > 0:
    print(min_h, max_h)


print("\nЗадание № 9")
while True:
    p1 = input("Придумайте пароль: ")
    p2 = input("Подтвердите пароль: ")
    if len(p1) < 8:
        print("Короткий!")
    elif "123" in p1:
        print("Простой!")
    elif p1 != p2:
        print("Различаются.")
    else:
        print("OK")
        break

#неправильно, но я другого не придумал
print("\nЗадание № 10")
while True:
    n1 = int(input())
    op = input().strip()
    
    if op == "x":
        print(n1)
        break
    
    if op == "!":
        if n1 >= 0:
            print(math.factorial(n1))
        continue # Переходим к следующей команде
    
    # Для остальных операций нужен второй ввод
    n2 = int(input())
    
    if op == "+": print(n1 + n2)
    elif op == "-": print(n1 - n2)
    elif op == "*": print(n1 * n2)
    elif op == "/":
        if n2 != 0: print(n1 // n2)
    elif op == "%":
        if n2 != 0: print(n1 % n2)


print("\nЗадание № 11")
h_pyr = int(input("Введите высоту пирамиды: "))
for i in range(1, h_pyr + 1):
    print(" " * (h_pyr - i) + "*" * (2 * i - 1))


print("\nЗадание № 12")
n_tree = int(input("Введите число N: "))
curr = 1
row_len = 1
while curr <= n_tree:
    for _ in range(row_len):
        if curr <= n_tree:
            print(curr, end=" ")
            curr += 1
    print()
    row_len += 1


print("\nЗадание № 13")
n_rect = int(input("Высота n: "))
m_rect = int(input("Ширина m: "))
symb = input("Символ: ")
for i in range(n_rect):
    if i == 0 or i == n_rect - 1:
        print(symb * m_rect)
    else:
        if m_rect > 1:
            print(symb + " " * (m_rect - 2) + symb)
        else:
            print(symb)