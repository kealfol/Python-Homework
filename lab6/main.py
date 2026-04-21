import math
import collections

# № 1
print("№ 1")
class BigBell:
    def __init__(self):
        self.at_ding = True
    def sound(self):
        if self.at_ding:
            print("ding")
        else:
            print("dong")
        self.at_ding = not self.at_ding

bell = BigBell()
bell.sound()
bell.sound()
bell.sound()

# № 2
print("\n№ 2")
class Balance:
    def __init__(self):
        self.left = 0
        self.right = 0
    def add_right(self, weight):
        self.right += weight
    def add_left(self, weight):
        self.left += weight
    def result(self):
        if self.left == self.right: return "="
        return "L" if self.left > self.right else "R"

balance = Balance()
balance.add_right(10)
balance.add_left(5)
balance.add_left(5)
print(balance.result())
balance.add_left(2)
print(balance.result())

# № 3
print("\n№ 3")
class Selector:
    def __init__(self, numbers):
        self.nums = numbers
    def get_odds(self):
        return [x for x in self.nums if x % 2 != 0]
    def get_evens(self):
        return [x for x in self.nums if x % 2 == 0]

values = [11, 12, 13, 14, 15, 16, 22, 44, 66]
sel = Selector(values)
print(*(sel.get_odds()))
print(*(sel.get_evens()))

# № 4
print("\n№ 4")
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __ne__(self, other):
        return not self.__eq__(other)

p1, p2 = Point(1, 2), Point(1, 2)
print(p1 == p2)
print(p1 != p2)

# № 5
print("\n№ 5")
class ReversedList:
    def __init__(self, lst):
        self.lst = lst
    def __len__(self):
        return len(self.lst)
    def __getitem__(self, index):
        return self.lst[-(index + 1)]

rl = ReversedList([10, 20, 30])
for i in range(len(rl)):
    print(rl[i])

# № 6
print("\n№ 6")
class SparseArray:
    def __init__(self):
        self.data = {}
    def __setitem__(self, key, value):
        if value == 0:
            if key in self.data: del self.data[key]
        else:
            self.data[key] = value
    def __getitem__(self, key):
        return self.data.get(key, 0)

arr = SparseArray()
arr[1] = 10
arr[8] = 20
for i in range(10):
    print(f"arr[{i}] = {arr[i]}")

# № 7
print("\n№ 7")
class Polynomial:
    def __init__(self, coeffs):
        self.coeffs = coeffs
    def __call__(self, x):
        return sum(c * (x**i) for i, c in enumerate(self.coeffs))
    def __add__(self, other):
        ln = max(len(self.coeffs), len(other.coeffs))
        new_c = []
        for i in range(ln):
            v1 = self.coeffs[i] if i < len(self.coeffs) else 0
            v2 = other.coeffs[i] if i < len(other.coeffs) else 0
            new_c.append(v1 + v2)
        return Polynomial(new_c)

p1 = Polynomial([10, -1])
print(p1(0), p1(1), p1(2))

# № 8
print("\n№ 8")
class Queue:
    def __init__(self, *args):
        self.items = list(args)
    def append(self, *values):
        self.items.extend(values)
    def copy(self):
        return Queue(*self.items)
    def pop(self):
        return self.items.pop(0) if self.items else None
    def extend(self, other):
        self.items.extend(other.items)
    def next(self):
        return Queue(*self.items[1:]) if self.items else Queue()
    def __add__(self, other):
        return Queue(*(self.items + other.items))
    def __iadd__(self, other):
        self.items.extend(other.items)
        return self
    def __eq__(self, other):
        return self.items == other.items
    def __rshift__(self, n):
        if n >= len(self.items): return Queue()
        return Queue(*self.items[n:])
    def __str__(self):
        if not self.items: return "[]"
        return "[" + " -> ".join(map(str, self.items)) + "]"
    def __next__(self):
        return self.next()

q = Queue(1, 2, 3)
print(q)
print(q >> 1)

# № 9
print("\n№ 9")
class Triangle:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c
    def perimeter(self):
        return self.a + self.b + self.c

class EquilateralTriangle(Triangle):
    def __init__(self, side):
        super().__init__(side, side, side)

print(EquilateralTriangle(5).perimeter())

# № 10
print("\n№ 10")
class Summator:
    def transform(self, n): return n
    def sum(self, N):
        return sum(self.transform(i) for i in range(1, N + 1))

class SquareSummator(Summator):
    def transform(self, n): return n**2

class CubeSummator(Summator):
    def transform(self, n): return n**3

print(SquareSummator().sum(3))

# № 11
print("\n№ 11")
class PowerSummator(Summator):
    def __init__(self, b):
        self.b = b
    def transform(self, n):
        return n ** self.b

class SquareSummator(PowerSummator):
    def __init__(self): super().__init__(2)

class CubeSummator(PowerSummator):
    def __init__(self): super().__init__(3)

print(PowerSummator(2).sum(3))

# № 12
print("\n№ 12")
class A:
    def __str__(self): return "A.__str__ method"
    def hello(self): print("Hello")

class B:
    def __str__(self): return "B.__str__ method"
    def good_evening(self): print("Good evening")

class C(A, B): pass
class D(B, A): pass

print(C())
print(D())

# № 13
print("\n№ 13")
class Weapon:
    def __init__(self, name, damage, range_):
        self.name, self.damage, self.range = name, damage, range_
    def __str__(self): return self.name

class BaseCharacter:
    def __init__(self, x, y, hp):
        self.x, self.y, self.hp = x, y, hp
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    def is_alive(self): return self.hp > 0
    def get_damage(self, amount):
        self.hp -= amount
    def get_coords(self): return (self.x, self.y)

class BaseEnemy(BaseCharacter):
    def __init__(self, x, y, weapon, hp):
        super().__init__(x, y, hp)
        self.weapon = weapon
    def hit(self, target):
        if not isinstance(target, MainHero):
            print("Могу ударить только Главного героя")
            return
        d = math.dist((self.x, self.y), (target.x, target.y))
        if d > self.weapon.range:
            print(f"Враг слишком далеко для оружия {self.weapon}")
        else:
            print(f"Враг нанес урон оружием {self.weapon} в размере {self.weapon.damage}")
            target.get_damage(self.weapon.damage)

class MainHero(BaseCharacter):
    def __init__(self, x, y, name, hp):
        super().__init__(x, y, hp)
        self.name = name
        self.inv = []
        self.wi = 0
    def add_weapon(self, w):
        if isinstance(w, Weapon):
            self.inv.append(w)
            print(f"Подобрал {w}")
        else: print("Это не оружие")
    def hit(self, target):
        if not self.inv:
            print("Я безоружен")
            return
        w = self.inv[self.wi]
        d = math.dist((self.x, self.y), (target.x, target.y))
        if d > w.range: print("Слишком далеко")
        else:
            print(f"Герой нанес урон {target} оружием {w}")
            target.get_damage(w.damage)
    def next_weapon(self):
        if not self.inv: print("Я безоружен")
        elif len(self.inv) == 1: print("У меня только одно оружие")
        else:
            self.wi = (self.wi + 1) % len(self.inv)
            print(f"Сменил оружие на {self.inv[self.wi]}")
    def heal(self, amount):
        self.hp = min(200, self.hp + amount)
        print(f"Полечился, теперь здоровья {self.hp}")
    def __str__(self): return self.name

# № 14
print("\n№ 14")
class MailServer:
    def __init__(self, name, servers_list):
        self.name = name
        self.allowed = servers_list
        self.boxes = collections.defaultdict(list)
    def receive(self, user, msg):
        self.boxes[user].append(msg)

class MailClient:
    def __init__(self, server, user):
        self.server, self.user = server, user
    def send_mail(self, srv, user, msg):
        if srv.name not in self.server.allowed:
            print(f"Ошибка: сервер {srv.name} недоступен")
        else:
            srv.receive(user, f"От {self.user}: {msg}")
    def receive_mail(self):
        m = self.server.boxes[self.user][:]
        self.server.boxes[self.user].clear()
        return m

# № 15
print("\n№ 15")
class Transformer:
    def __init__(self, nums):
        self.nums = nums
        self.ops = {
            "make_negative": (lambda x: x > 0, lambda x: x * -1),
            "square": (lambda x: True, lambda x: x ** 2),
            "strange_command": (lambda x: x % 5 == 0, lambda x: x + 1)
        }
    def apply(self, cmd):
        if cmd in self.ops:
            cond, act = self.ops[cmd]
            self.nums = [act(x) if cond(x) else x for x in self.nums]
    def __str__(self): return " ".join(map(str, self.nums))

t = Transformer([1, 0, -2, 30, -4])
t.apply("make_negative")
print(t)

# № 16
print("\n№ 16")
class FuncObj:
    def __init__(self, f): self.f = f
    def __call__(self, x): return self.f(x)

class Evaluator:
    def __init__(self):
        self.funcs = {'x': FuncObj(lambda x: x), 'sqrt_fun': FuncObj(math.sqrt)}
    def define(self, name, arg1, op, arg2):
        f1, f2 = self.funcs[arg1], self.funcs[arg2]
        if op == '+': self.funcs[name] = FuncObj(lambda x: f1(x) + f2(x))
        if op == '*': self.funcs[name] = FuncObj(lambda x: f1(x) * f2(x))
    def calculate(self, name, vals):
        return [round(self.funcs[name](float(v)), 2) for v in vals]

ev = Evaluator()
ev.define("f1", "x", "*", "x")
print(ev.calculate("f1", [1, 2, 3]))

# № 17
print("\n№ 17 (Планировщик конференций)")


class Доклад:
    def __init__(self, тема, начало, длительность):
        self.тема = тема
        self.начало = начало
        self.длительность = длительность
        self.конец = начало + длительность

    def __str__(self):
        return f"'{self.тема}' (Начало: {self.начало}, Конец: {self.конец})"


class Конференция:
    def __init__(self):
        self.список_докладов = []

    def добавить_доклад(self, новый_доклад):
        перекрытия = []
        for d in self.список_докладов:
            if not (новый_доклад.конец <= d.начало or новый_доклад.начало >= d.конец):
                перекрытия.append(d.тема)

        if перекрытия:
            print(
                f"\n[!] ПРЕДУПРЕЖДЕНИЕ: Доклад '{новый_доклад.тема}' пересекается по времени с: {', '.join(перекрытия)}")

        self.список_докладов.append(новый_доклад)
        self.список_докладов.sort(key=lambda x: x.начало)
        print(f"Доклад '{новый_доклад.тема}' успешно добавлен.")

    def суммарное_время(self):
        return sum(d.длительность for d in self.список_докладов)

    def максимальный_перерыв(self):
        if len(self.список_докладов) < 2:
            return 0

        макс_пауза = 0
        for i in range(len(self.список_докладов) - 1):
            пауза = self.список_докладов[i + 1].начало - self.список_докладов[i].конец
            if пауза > макс_пауза:
                макс_пауза = пауза
        return макс_пауза

    def показать_расписание(self):
        if not self.список_докладов:
            print("\nРасписание пока пусто.")
            return
        print("\n--- Текущее расписание ---")
        for d in self.список_докладов:
            print(d)


conf = Конференция()

print("Добро пожаловать в систему планирования конференции!")
print("Команды: 'add' - добавить доклад, 'info' - статистика, 'list' - расписание, 'exit' - выход.")

while True:
    cmd = input("\nВведите команду: ").lower().strip()

    if cmd == 'add':
        try:
            tema = input("Введите тему доклада: ")
            start = float(input("Введите время начала (например, 10.5 для 10:30): "))
            duration = float(input("Введите длительность в часах (например, 1.5): "))

            nov_doklad = Доклад(tema, start, duration)
            conf.добавить_доклад(nov_doklad)
        except ValueError:
            print("Ошибка: время и длительность должны быть числами.")

    elif cmd == 'info':
        print(f"\nОбщая продолжительность всех докладов: {conf.суммарное_время()} ч.")
        print(f"Самый долгий перерыв между докладами: {conf.максимальный_перерыв()} ч.")

    elif cmd == 'list':
        conf.показать_расписание()

    elif cmd == 'exit':
        print("Завершение работы.")
        break
    else:
        print("Неизвестная команда. Используйте add, info, list или exit.")

# № 18
print("\n№ 18")
class FileSystem:
    def __init__(self):
        self.fs = {"/": {"type": "dir", "children": {}}}
    def _navigate(self, path, create=False):
        curr = self.fs["/"]
        parts = [p for p in path.split("/") if p]
        for p in parts:
            if p not in curr["children"]:
                if create: curr["children"][p] = {"type": "dir", "children": {}}
                else: return None
            curr = curr["children"][p]
        return curr
    def mkdir(self, path): self._navigate(path, True)
    def write(self, path, text):
        ps = path.split("/")
        d = self._navigate("/".join(ps[:-1]), True)
        d["children"][ps[-1]] = {"type": "file", "data": text}
    def read(self, path):
        f = self._navigate(path)
        return f["data"] if f and f.get("type") == "file" else "Not found"
    def ls(self, path):
        d = self._navigate(path)
        return sorted(d["children"].keys()) if d else []

fs = FileSystem()
fs.mkdir("docs/work")
fs.write("docs/work/1.txt", "Report data")
print(fs.ls("docs/work"))
print(fs.read("docs/work/1.txt"))