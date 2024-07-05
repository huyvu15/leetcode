a = "aaAbcBC"

b = set()


for char in a:
    if char.lower() in a and char.upper() in a:
        b.add(char.lower())

print(len(b))