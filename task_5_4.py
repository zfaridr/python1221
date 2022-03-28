src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result = list(
    filter(lambda x:
           x > src[src.index(x) - 1] and src.index(x) != 0,
           src)
)

print(result)


