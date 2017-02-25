def square(num):
	square = num**2
	return square

x = range(5)

squared = map(square, x)
print(squared)


