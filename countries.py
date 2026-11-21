dict1 = {'India' : '0091', 'Australia' : '0025', 'Nepal' : '00977'}

print(dict1)
    
country = (input('Please enter a country name: '))

print(dict1.get(country,'Value for this key is not found in the dictionary '))



