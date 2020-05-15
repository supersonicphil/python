

number = 7
guesses = 1


while guesses <=5:

	guess=int(input('im thinking of a number between 1 and 8. can you guess a number?: '))

	if guess == number:
		print('well done')
		break
	elif guess <= number:
		print('to low')
	elif guess >= number:
		print('too high')

	guesses = guesses + 1

if guess != number:
	print('unlucky try again next time')

