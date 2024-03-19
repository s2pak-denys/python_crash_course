for value in range(1, 1_000_001):
	print(value)

nambers = list(range(1, 1_000_001))
digits = nambers
print(sum(digits))
print(min(nambers))
print(max(nambers))
print(sum(nambers))

#print(max(digits))
#print(min(digits))
#print(sum(digits))

squares = []
for value in range(1, 11):
	square = value ** 2
	squares.append(square)
print(squares)

odd_numbers = list(range(1, 20, 2))
print(odd_numbers)

t_numbers = list(range(3, 33, 3))
print(t_numbers)

#в третьому степені
squares = []
for value in range(1, 10):
	square = value ** 3
	squares.append(square)
print(squares)

#куби генераторним списком
squares = [value ** 3 for value in range(1, 10)]
print(squares)