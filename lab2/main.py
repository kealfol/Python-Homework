import collections

# № 1
print("№ 1")
s = "Abrakadabra"
print(s[2])
print(s[-2])
print(s[:5])
print(s[:-2])
print(s[::2])
print(s[1::2])
print(s[::-1])
print(s[::-2])
print(len(s))

# № 2
print("\n№ 2")
s = "загогулина"
mid = (len(s) + 1) // 2
print(s[mid:] + s[:mid])

# № 3
print("\n№ 3")
s = "In the hole in the ground there lived a hobbit"
f = s.find('h')
l = s.rfind('h')
print(s[:f] + s[f:l + 1][::-1] + s[l + 1:])

# № 4
print("\n№ 4")
s = "office"
f = s.find('f')
l = s.rfind('f')
if f != -1:
    if f == l:
        print(f)
    else:
        print(f, l)

# № 5
print("\n№ 5")
words_list = ["новгород", "дублин", "новгород", "дублин", "тула"]
prev = words_list[0]
for i in range(1, len(words_list)):
    curr = words_list[i]
    if curr[0] != prev[-1]:
        print(curr)
        break
    prev = curr

# № 6
print("\n№ 6")
word = "медленнее"
for i in range(len(word)):
    print(word[i] * (i + 1), end='')
print()

# № 7
print("\n№ 7")
line = "@VV>>>>>>>VV<<<<VV>>>"
char = line[0]
path = line[1:]
points = [(0, 0)]
cx, cy = 0, 0
for m in path:
    if m == '>': cx += 1
    elif m == '<': cx -= 1
    elif m == 'V': cy += 1
    points.append((cx, cy))
mx_y = max(p[1] for p in points)
mx_x = max(p[0] for p in points)
grid = [[' ' for _ in range(mx_x + 1)] for _ in range(mx_y + 1)]
for x, y in points:
    grid[y][x] = char
for row in grid:
    print("".join(row).rstrip())

# № 8
print("\n№ 8")
word = "рогатка"
n = len(word)
if n % 2 == 1:
    mid = n // 2
    for i in range(mid + 1):
        l, r = mid - i, mid + i
        if l == r: print(' ' * l + word[mid])
        else: print(' ' * l + word[l] + ' ' * (r - l - 1) + word[r])
else:
    m2 = n // 2
    m1 = m2 - 1
    for i in range(m2):
        l, r = m1 - i, m2 + i
        print(' ' * l + word[l] + ' ' * (r - l - 1) + word[r])

# № 9
print("\n№ 9")
nums = [1, 5, 2, 4, 3]
for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        print(nums[i], end=' ')
print()

# № 10
print("\n№ 10")
nums = [-1, 2, 3, -1, -2]
for i in range(len(nums) - 1):
    if (nums[i] > 0 and nums[i+1] > 0) or (nums[i] < 0 and nums[i+1] < 0):
        print(nums[i], nums[i+1])
        break

# № 11
print("\n№ 11")
arr = ["1", "2", "3", "4", "5"]
for i in range(0, len(arr) - 1, 2):
    arr[i], arr[i+1] = arr[i+1], arr[i]
print(" ".join(arr))

# № 12
print("\n№ 12")
arr = ["1", "2", "2", "3", "3", "3", "4"]
for x in arr:
    if arr.count(x) == 1:
        print(x, end=' ')
print()

# № 13
print("\n№ 13")
idxs = [4, 3, 1]
text = "Буря мглою небо кроет".split()
res = [text[i-1].lower() for i in idxs]
print(" ".join(res).capitalize())

# № 14
print("\n№ 14")
coords = [(1, 8), (2, 7), (3, 6), (4, 5), (5, 4), (6, 3), (7, 2), (8, 1)]
x = [c[0] for c in coords]; y = [c[1] for c in coords]
hit = False
for i in range(8):
    for j in range(i + 1, 8):
        if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
            hit = True
print("YES" if hit else "NO")

# № 15
print("\n№ 15")
events = [
    "Кто последний? Я - Кузнецов.",
    "Кто последний? Я - Поливанов.",
    "Следующий!",
    "Я только спросить! Я - Иванова.",
    "Следующий!",
    "Следующий!",
    "Следующий!"
]
q = collections.deque()
for e in events:
    if "Кто последний?" in e:
        q.append(e.split(" - ")[1].strip('.'))
    elif "Я только спросить!" in e:
        q.appendleft(e.split(" - ")[1].strip('.'))
    elif "Следующий!" in e:
        if q: print(f"Заходит {q.popleft()}!")
        else: print("В очереди никого нет.")