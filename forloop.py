family=['sam', 'izzy', 'polly']

for i in family:
	print(i.title() + ' Good afternoon!')

print('\nits good to see you all!!!')



for i in range(1,5):
	print(i)


#numbers = list(range(1,10000000))
#print(numbers)

squares = []
for value in range(1,11):
	square = value**2
	squares.append(value**2)

print(squares)



squares = [value**2 for value in range (1, 11)]
print(squares)

digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))







num = list(range(0,31, 3))
print(num)

powerof = [value**3 for value in range (1, 11)]
print(powerof)