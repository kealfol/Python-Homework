import collections

# № 1
print("№ 1")
numbers = [1, 2, 3, 2, 1]
print(len(set(numbers)))

# № 2
print("\n№ 2")
list1 = [1, 3, 2]
list2 = [4, 3, 2]
print(len(set(list1) & set(list2)))

# № 3
print("\n№ 3")
list1 = [1, 3, 2]
list2 = [4, 3, 2]
print(*sorted(set(list1) & set(list2)))

# № 4
print("\n№ 4")
sequence = [1, 2, 3, 2, 3, 4]
seen = set()
for num in sequence:
    if num in seen:
        print("YES")
    else:
        print("NO")
        seen.add(num)

# № 5
print("\n№ 5")
text_lines = [
    "She sells sea shells on the sea shore;",
    "The shells that she sells are sea shells I'm sure.",
    "So if she sells sea shells on the sea shore,",
    "I'm sure that the shells are sea shore shells."
]
words = set()
for line in text_lines:
    words.update(line.split())
print(len(words))

# № 6
print("\n№ 6")
surnames = ["Иванов", "Петров", "Сидоров", "Петров", "Иванов", "Петров"]
counts = collections.Counter(surnames)
total_duplicates = 0
for name in counts:
    if counts[name] > 1:
        total_duplicates += counts[name]
print(total_duplicates)

# № 7
print("\n№ 7")
text = "one two one two three"
word_counts = {}
for word in text.split():
    print(word_counts.get(word, 0), end=' ')
    word_counts[word] = word_counts.get(word, 0) + 1
print()

# № 8
print("\n№ 8")
synonyms_raw = [("Hello", "Hi"), ("Bye", "Goodbye"), ("List", "Array")]
target_word = "Goodbye"
syn_dict = {}
for word1, word2 in synonyms_raw:
    syn_dict[word1] = word2
    syn_dict[word2] = word1
print(syn_dict.get(target_word))

# № 9
print("\n№ 9")
votes_data = [
    "Ivanov 10",
    "Ivanov 5",
    "Sidorov 9",
    "Sidorov 8",
    "Ivanov 1"
]
candidates = {}
for entry in votes_data:
    name, count = entry.split()
    candidates[name] = candidates.get(name, 0) + int(count)

for name in sorted(candidates):
    print(name, candidates[name])

# № 10
print("\n№ 10")
files_permissions = {
    "helloworld.exe": {"R", "X"},
    "pinglog": {"W", "R"},
    "nya": {"R"},
    "goodluck": {"X", "W", "R"}
}
queries = [
    ("read", "nya"),
    ("write", "helloworld.exe"),
    ("execute", "nya"),
    ("read", "pinglog"),
    ("write", "pinglog")
]

cmd_to_perm = {
    "read": "R",
    "write": "W",
    "execute": "X"
}

for cmd, filename in queries:
    if cmd_to_perm[cmd] in files_permissions.get(filename, set()):
        print("OK")
    else:
        print("Access denied")