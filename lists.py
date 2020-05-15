
newlist = ['phil', 'izzy', 'sam', 'polly', 'jeff']

print (newlist[1])

print('Hello ' + newlist[0].title())
print('Hello ' + newlist[1].title())
print('Hello ' + newlist[2].title())
print('Hello ' + newlist[3].title())
print('Hello ' + newlist[4].title())



guitars = ['fender', 'gibson', 'epipone']

print(guitars)

print('i have a ' + guitars[0].title() + ' Stratocatster')
print('i also have a ' + guitars[-1].title() + ' SG')
print('I would love a real ' + guitars[1].title() + ' to own myself one day')


guitars[0] = 'yamaha'
print(guitars)
guitars[0] = 'fender'
print(guitars)

guitars.append('yamaha')
print(guitars)

tech = []

tech.append('cisco')
tech.append('azure')
tech.append('python')

print(tech)

tech.insert(1, 'aws')

print(tech)

popped_tech = tech.pop(2)
print(tech)
print(popped_tech)
print('the last course i did was ' + popped_tech)


sweets=['bonbon', 'mint', 'toffee']
print(sweets)
sweets.remove('mint')
print(sweets)




guests=['liam', 'noel', 'hendrix']
print('Hi ' + guests[0].title() + ' you are invited to my dinner')
print('Hi ' + guests[1].title() + ' you are invited to my dinner')
print('Hi ' + guests[2].title() + ' you are invited to my dinner')

print('\nim so sorry ' + guests[1].title() + ' can not make the date')

guests[1]=('lennon')
print(guests)


print('Hi ' + guests[0].title() + ' you are invited to my dinner')
print('Hi ' + guests[1].title() + ' you are invited to my dinner')
print('Hi ' + guests[2].title() + ' you are invited to my dinner')

print('\nHi All we have now found a bigger table')

guests.insert(0, 'Hank')
guests.insert(2, 'bonehead')
guests.insert(5, 'guiggs')

print(guests)
print(len(guests))


print('Hi ' + guests[0].title() + ' you are invited to my dinner')
print('Hi ' + guests[1].title() + ' you are invited to my dinner')
print('Hi ' + guests[2].title() + ' you are invited to my dinner')
print('Hi ' + guests[3].title() + ' you are invited to my dinner')
print('Hi ' + guests[4].title() + ' you are invited to my dinner')
print('Hi ' + guests[5].title() + ' you are invited to my dinner')

poppedguest = guests.pop(5)
print(guests)
print('im very sorry ' + poppedguest + ' we have just been informed the table wont arrive in time')
poppedguest=guests.pop(4)
print(guests)
print('im very sorry ' + poppedguest + ' we have just been informed the table wont arrive in time')
poppedguest=guests.pop(3)
print(guests)
print('im very sorry ' + poppedguest + ' we have just been informed the table wont arrive in time')
poppedguest=guests.pop(2)
print(guests)
print('im very sorry ' + poppedguest + ' we have just been informed the table wont arrive in time')

del guests[1]
print(guests)
del guests[0]
print(guests)



cars=['citreon', 'bmw', 'aldi', 'nissan', 'mini']
print(cars)
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

dogs=['shih tzu', 'jack russell', 'terrier', 'bulldog']
print(dogs)
print(sorted(dogs))

dogs.reverse()
print(dogs)
len=len(dogs)
print(len)



visit=['new york', 'pyrimids', 'australia', 'russia', 'iceland']
print(visit)
print(sorted(visit))
print(visit)
visit.reverse()
print(visit)
visit.reverse()
print(visit)
visit.sort()
print(visit)
visit.sort()
print(visit)


print()





