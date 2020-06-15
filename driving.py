country = input('which country: ')
age = input('How old are you: ')
age = int(age)
#
if country == 'Taiwan':
	if age >= 18:
		print('you could drive a car')
	else:
	    print('you could not drive a car')	
elif country == 'USA':
	if age >= 16:
		print('you could drive a car in USA')
	else:
	    print('You could not drive in USA')	
else:
    print('You could only type Taiwan and USA')	    