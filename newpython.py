name = input('What is your name?: ')
age = int(input('what is your age?: '))
print('your name is' + ' ' + name + ' and you are ' + str(age) + ' years old')
newage = int(age+10)
print('in 10 years time your will be ' + str(newage))

newyear = int(input('choose a number to find out how old you will be: '))
newage = int(age+newyear)
print('in ' + str(newyear) + ' years you will be ' + str(newage) )

daughter=input('What is your daughters name?: ')
daughterage=int(input('How old is your daughter in years?: '))
print('your daughters name is ' + daughter + ' and her age is ' + str(daughterage))

daughteragenew = int(newyear+daughterage)
print(" ")
print('So you will be ' + str(newage) + ' and ' + daughter + ' will be ' + str(daughteragenew))

animal = input('Do you have a dog or a cat? or both?: ')

if animal == 'dog':
	print('you have a dog')
elif animal == 'cat':
	print ('you have a cat')
elif animal == 'both':
	print('you have a dog and a cat')

else:
	print('You do not have a cat or a dog')

wife = input('Do you have a wife? : ')

if wife == 'yes':
	wifename = input('What is her name? ')
	print('your wifes name is ' + wifename)
else:
	print('you do not have a wife')

wifeage = int(input('How old is your wife? '))
print('you are ' + str(age) + ' and your wife is ' + str(wifeage) + ' and your daughter is ' + str(daughterage) + '\nIn ' + str(newyear) + ' years time, you will be ' + str(newage) + ' and ' +  wifename + ' will be ' + str(wifeage+newyear) + ' and ' + daughter + ' will be ' + str(daughteragenew))

