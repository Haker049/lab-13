import math

pairs = [(2, 4), (4, 6), (0, 1), (5, 2), (9, 1), (3, 8)]

sus = []

for i in pairs:
    i = math.prod(i)
    sus.append(i)
calc = {}
for i in range(len(pairs)):
    calc[pairs[i]] = sus[i]

print(calc)