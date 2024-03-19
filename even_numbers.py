even_numbers = list(range(2, 11, 2))
print(even_numbers)

#test_v1
odd_numbers = list(range(1, 20, 2))
print(odd_numbers)

t_numbers = list(range(3, 33, 3))
print(t_numbers)

squares = []
for value in range(1, 10):
	square = value ** 3
	squares.append(square)
print(squares)

squares = [value ** 3 for value in range(1, 10)]
print(squares)