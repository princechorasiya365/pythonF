L = [y - x for x in [1, 2, 3] for y in [3, 4, 5] if y > x]
print(L)

L = [ ]
for x in [1, 2, 3]:
    for y in [3, 4, 5]:
        if y > x:
            L.append(y - x)
print(L)

L = [ ]
for y in [3, 4, 5]:
    for x in [1, 2, 3]:
        if y > x:
            L.append(y - x)
print(L)