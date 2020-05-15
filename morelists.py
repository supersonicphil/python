list = ['phil', 'sam', 'izzy', 'polly', 'munch']
print(list[-3])

print('here are the first 3 names : ')
for name in list[3:]:
	print(name.title())



newlist=['chilli', 'chocolate', 'prezels', 'sweets']

for food in newlist[:2]:
	print(food)


newlist=['chilli', 'chocolate', 'prezels', 'sweets', 'mints', 'bonbon']
friemdsfoods=newlist[:]
newlist.append('pasta')
friemdsfoods.append('rice')
print(newlist)
print(friemdsfoods)

print('The first three items in the list are: ' + str(newlist[0:3]))
print('Three items in the middle of the list are: ' + str(newlist[2:5]))
print('The last three items in the list are: ' + str(newlist[3:7]))



mypizza=['chilli', 'margarita', 'ham', 'meatfeast']
sampizza=mypizza[:]
mypizza.append('cheese')
sampizza.append('mushroom')
print(sampizza)
print('My favorite pizzas are: ')
for pizza in mypizza:
	print(pizza)

print('Sams favorite pizzas are: ')
for pizza in sampizza:
		print(pizza)
