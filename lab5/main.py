import math
import functools
import sys

# № 1
print("№ 1")
my_list = [1, 2, 10, 15, 20, 3, 5, 18, 2, 27, 45, 99]
print(list(filter(lambda x: x < 5, my_list)))
print(list(map(lambda x: x / 2, my_list)))
print(list(map(lambda x: x / 2, filter(lambda x: x > 17, my_list))))
res4 = sum(map(lambda x: x**2, filter(lambda x: 10 <= x <= 99 and x % 9 == 0, range(100))))
print(res4)

# № 2
print("\n№ 2")
def factorials(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
        yield res

print(*factorials(7))

# № 3
print("\n№ 3")
def square_fibonacci(n):
    a, b = 1, 1
    for _ in range(n):
        yield a**2
        a, b = b, a + b

print(*square_fibonacci(7))

# № 4
print("\n№ 4")
def russian_alphabet():
    for i in range(ord('а'), ord('я') + 1):
        yield chr(i)

print(*russian_alphabet())

# № 5
print("\n№ 5")
alphabet_gen = (chr(i) for i in range(ord('а'), ord('я') + 1))
print(*alphabet_gen)

# № 6
print("\n№ 6")
def arithmetic_operation(operation):
    if operation == '+': return lambda x, y: x + y
    if operation == '-': return lambda x, y: x - y
    if operation == '*': return lambda x, y: x * y
    if operation == '/': return lambda x, y: x / y

op = arithmetic_operation('+')
print(op(1, 4))

# № 7
print("\n№ 7")
def same_by(characteristic, objects):
    if not objects: return True
    first = characteristic(objects[0])
    return all(characteristic(x) == first for x in objects)

values1 = [0, 2, 10, 6]
print("same" if same_by(lambda x: x % 2, values1) else "different")
values2 = [1, 2, 3, 4]
print("same" if same_by(lambda x: x % 2, values2) else "different")

# № 8
print("\n№ 8")
def print_operation_table(operation, num_rows=9, num_columns=9):
    for r in range(1, num_rows + 1):
        row_data = [str(operation(r, c)) for c in range(1, num_columns + 1)]
        print("\t".join(row_data))

print_operation_table(lambda x, y: x * y, 5, 5)

# № 9
print("\n№ 9")
def ask_password(login, password, success, failure):
    vowels = "aeiouy"
    pass_vowels = [c for c in password.lower() if c in vowels]
    pass_cons = [c for c in password.lower() if c not in vowels]
    login_cons = [c for c in login.lower() if c not in vowels]

    v_ok = len(pass_vowels) == 3
    c_ok = pass_cons == login_cons

    if v_ok and c_ok:
        success(login)
    elif not v_ok and not c_ok:
        failure(login, "Everything is wrong")
    elif not v_ok:
        failure(login, "Wrong number of vowels")
    else:
        failure(login, "Wrong consonants")

def main(login, password):
    def success_cb(l): print(f"Привет, {l}!")
    def failure_cb(l, err): print(f"Кто-то пытался притвориться пользователем {l}, но в пароле допустил ошибку: {err.upper()}.")
    ask_password(login, password, success_cb, failure_cb)

main("Ivan", "nsyatos")
main("eugene", "aanig")

# № 10
print("\n№ 10")
s_in = "cats dog CAT DOGGY monkey"
print(*(sorted(s_in.split(), key=lambda x: x.lower())))

# № 11
print("\n№ 11")
nums = [3, 6, -8, 2, -78, 1, 23, -45, 9]
print(*(sorted(nums, key=lambda x: abs(x), reverse=True)))

# № 12
print("\n№ 12")
points = [(1, 1), (0, 2), (2, 0), (0, 0), (1, 0)]
print(sorted(points, key=lambda p: (p[0]**2 + p[1]**2, p[0], p[1])))

# № 13
print("\n№ 13")
table = [[1, 2, 3], [4, 0, 6], [7, 8, 9]]
print(any(0 in row for row in table))

# № 14
print("\n№ 14")
text = """Ехал Грека через реку.
Видит Грека в реке рак.
Сунул в реку руку Грека.
Рак за руку Греку цап."""
all_words = []
for line in text.splitlines():
    all_words.extend(line.replace('.', '').replace(',', '').split())

first_occ = {}
for i, w in enumerate(all_words):
    if w not in first_occ:
        first_occ[w] = i

up_words = sorted({w for w in all_words if w[0].isupper()})
for w in up_words:
    print(f"{first_occ[w]} - {w}")

# № 15
print("\n№ 15")
lines = ["котик", "тюлень", "кашалот", "нарвал"]
print(functools.reduce(lambda a, b: a if a < b else b, lines))

# № 16
print("\n№ 16")
nums_gcd = [36, 12, 144, 18]
print(functools.reduce(math.gcd, nums_gcd))

# № 17
print("\n№ 17")
def check_password_simple(func):
    def wrapper(*args, **kwargs):
        p = "1234"
        if p == "1234": return func(*args, **kwargs)
        print("В доступе отказано")
        return None
    return wrapper

@check_password_simple
def secret(): print("Доступ открыт")
secret()

# № 18
print("\n№ 18")
def check_password(password_to_check):
    def decorator(func):
        def wrapper(*args, **kwargs):
            entered = password_to_check
            if entered == password_to_check: return func(*args, **kwargs)
            return None
        return wrapper
    return decorator

@check_password('password')
def make_burger(): print("Бургер готов")
make_burger()

# № 19
print("\n№ 19")
def cached(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@cached
def fib(n):
    if n <= 2: return 1
    return fib(n - 1) + fib(n - 2)

print(fib(10))