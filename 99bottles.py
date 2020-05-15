


n = 100


while n > -1:

    if n == 1:
        print('There is ' + str(n) + ' bottle of beer on the wall...pass the last one round')
        n = n -1
        print('There are ' + str(n)  + ' more beers left')
        
        
    elif n == 0:
        print('There are no more beers so go to the shop and buy some more')
        break
    else:
        
        print ('there are ' + str(n) + ' bottles of beer on the wall..pass one round')
        n = n -1
        print('now there are only ' + str(n) + ' beers on the wall')    
    
    
