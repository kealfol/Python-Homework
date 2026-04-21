import math

# № 1
print("№ 1")
my_list = [1, 10, 15, 20, 3, 5, 18, 2]
print([x for x in my_list if x < 5])
print([x / 2 for x in my_list])
print([x * 2 for x in my_list if x > 17])
n_val = 5
print([x ** 2 for x in range(n_val + 1)])
input_str = "1 2 3 4 5"
print(*(int(x) ** 2 for x in input_str.split()))
input_str_2 = "1 2 3 4 5 6 7 8 9 10"
print(*(sq for x in input_str_2.split() if (sq := int(x) ** 2) % 2 != 0 and sq % 10 != 9))

# № 2
print("\n№ 2")
data_in = "3 7 1 10 8"
print("\n".join("*" * int(x) for x in data_in.split()))

# № 3
print("\n№ 3")


def triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print("Это треугольник")
    else:
        print("Это не треугольник")


triangle(1, 1, 2)
triangle(7, 6, 10)
triangle(20, 13, 17)

# № 4
print("\n№ 4")


def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


print(distance(0, 0, 3, 4))

# № 5
print("\n№ 5")


def number_to_words(n):
    ones = ["ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять",
            "десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать",
            "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
    tens = ["", "", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
    if n < 20:
        return ones[n]
    else:
        return tens[n // 10] + (" " + ones[n % 10] if n % 10 != 0 else "")


print(number_to_words(4))
print(number_to_words(13))

# № 6
print("\n№ 6")


def bracket_check(test_string):
    balance = 0
    for char in test_string:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
        if balance < 0: break
    print("YES" if balance == 0 else "NO")


bracket_check("()")
bracket_check("(()((")

# № 7
print("\n№ 7")


def palindrome(s):
    clean_s = "".join(s.lower().split())
    if clean_s == clean_s[::-1]:
        return "Палиндром"
    return "Не палиндром"


print(palindrome("А роза упала на лапу Азора"))
print(palindrome("Палиндром"))

# № 8
print("\n№ 8")


def tic_tac_toe(field):
    lines = field + list(zip(*field))
    lines.append([field[i][i] for i in range(3)])
    lines.append([field[i][2 - i] for i in range(3)])

    x_win = any(all(cell == 'x' for cell in line) for line in lines)
    o_win = any(all(cell == '0' for cell in line) for line in lines)

    if x_win:
        print("x win")
    elif o_win:
        print("0 win")
    else:
        print("draw")


field_example = [['0', '-', '0'], ['x', 'x', 'x'], ['0', '0', '-']]
tic_tac_toe(field_example)

# № 9
print("\n№ 9")
last_message = None


def print_without_duplicates(message):
    global last_message
    if message != last_message:
        print(message)
        last_message = message


print_without_duplicates("Привет")
print_without_duplicates("Не могу до тебя дозвониться")
print_without_duplicates("Не могу до тебя дозвониться")
print_without_duplicates("Ага, жду")

# № 10
print("\n№ 10")
friends_db = {}


def add_friends(name, friends_list):
    if name not in friends_db: friends_db[name] = set()
    for friend in friends_list:
        friends_db[name].add(friend)
        if friend not in friends_db: friends_db[friend] = set()
        friends_db[friend].add(name)


def are_friends(n1, n2):
    return n2 in friends_db.get(n1, set())


def print_friends(name):
    print(*(sorted(friends_db.get(name, []))))


add_friends("Алла", ["Марина", "Иван"])
print(are_friends("Алла", "Мария"))
add_friends("Алла", ["Мария"])
print(are_friends("Алла", "Мария"))

# № 11
print("\n№ 11")
one = 5
two = 4


def roman():
    def to_roman(num):
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        res = ""
        for i in range(len(val)):
            while num >= val[i]:
                res += syb[i]
                num -= val[i]
        return res

    three = one + two
    print(f"{to_roman(one)} + {to_roman(two)} = {to_roman(three)}")


roman()

# № 12
print("\n№ 12")
v1 = [1, 2];
v1 = v1 + [3]
v2 = [1, 2];
v2 += [3]
print("Демонстрация изменяемости в комментариях кода.")

# № 13
print("\n№ 13")
arr = [3, 1, 2]
sorted_arr = sorted(arr)
print(f"Original after sorted(): {arr}")
arr.sort()  # Сортирует на месте
print(f"Original after sort(): {arr}")

# № 14
print("\n№ 14")
numbers = [2, 5, 7, 7, 8, 4, 1, 6]
odd = []
even = []
for number in numbers:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)
print(f"Even: {even}, Odd: {odd}")

# № 15
print("\n№ 15")
fractal = [0, None, None, 2]
fractal[1] = fractal
fractal[2] = fractal

# № 16
print("\n№ 16")


def continue_fibonacci_sequence(sequence, n):
    for _ in range(n):
        next_element = sequence[-1] + sequence[-2]
        sequence.append(next_element)


seq = [1, 1]
continue_fibonacci_sequence(seq, 1)
print(*seq)

# № 17
print("\n№ 17")


def mirror(arr):
    mirrored_part = arr[::-1]
    arr.extend(mirrored_part)


a_mirror = [1, 2]
mirror(a_mirror)
print(*a_mirror)

# № 18
print("\n№ 18")


def from_string_to_list(string, container):
    container.extend(int(x) for x in string.split())


a_cont = [1, 2, 3]
from_string_to_list("1 3 99 52", a_cont)
print(*a_cont)

# № 19
print("\n№ 19")


def transpose(matrix):
    res = [list(row) for row in zip(*matrix)]
    matrix.clear()
    matrix.extend(res)


mat = [[1, 2], [3, 4]]
transpose(mat)
for r in mat: print(*r)

# № 20
print("\n№ 20")


def swap(first, second):
    tmp = first[:]
    first[:] = second[:]
    second[:] = tmp[:]


f_list, s_list = [1, 2], [4, 5]
swap(f_list, s_list)
print(f_list, s_list)

# № 21
print("\n№ 21")


def defractalize(fractal):
    i = 0
    while i < len(fractal):
        if fractal[i] is fractal:
            fractal.pop(i)
        else:
            i += 1


f_frac = [2, 5];
f_frac.append(f_frac);
f_frac.append(3)
defractalize(f_frac)
print(f_frac)

# № 22
print("\n№ 22")


def fractal_print(obj):
    def clean(item):
        return "[...]" if item is obj else item

    print([clean(x) for x in obj])


f_obj = [3];
f_obj.append(f_obj)
fractal_print(f_obj)

# № 23
print("\n№ 23")


def matrix(n=1, m=None, a=0):
    if m is None: m = n
    return [[a] * m for _ in range(n)]


print(matrix())
print(matrix(2))

# № 24
print("\n№ 24")


def partial_sums(*args):
    res = [0]
    current = 0
    for x in args:
        current += x
        res.append(current)
    return res


print(partial_sums(1, 0.5, 0.25))

# № 25
print("\n№ 25")


def solve(*coeffs):
    if len(coeffs) == 3:
        a, b, c = coeffs
        if a == 0: return solve(b, c)
        d = b ** 2 - 4 * a * c
        if d < 0: return []
        if d == 0: return [-b / (2 * a)]
        return [(-b - math.sqrt(d)) / (2 * a), (-b + math.sqrt(d)) / (2 * a)]
    elif len(coeffs) == 2:
        b, c = coeffs
        if b == 0: return ["all"] if c == 0 else []
        return [-c / b]
    elif len(coeffs) == 1:
        return ["all"] if coeffs[0] == 0 else []
    return None


print(sorted(solve(1, 2, 1)))
print(sorted(solve(1, -3, 2)))