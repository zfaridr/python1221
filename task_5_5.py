src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

result1 = []
for i in src:
    if i not in src[src.index(i)+1:]:
        result1.append(i)

print(result1)

result2 = list(
    filter(
        lambda x: x not in src[src.index(x)+1:],
        src)
)

print(result2)


