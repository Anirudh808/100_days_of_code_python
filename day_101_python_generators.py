def squares(length):
    for n in range(length):
        yield n ** 2


for square in squares(5):
    print(square)

squares_1 = (n ** 2 for n in range(5))

print(squares_1)
