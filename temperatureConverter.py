# temperature conversion between celcius and kelivn is "273"
# hence I will assign the constant to  C

C = 273


 
print('Welcome to this temperature converter, pick one to convert: C-K or K-C')
Convert = None

while Convert != 'K-C' or 'C-K':
    
    if Convert != 'K-C' or 'C-K':
        print("Wrong values!. Input a valid conversion line")
        Convert = input('Choose either C-K or K-C: ').upper()
    
    if Convert == 'C-K': 
        UserTemp = float(input('Enter the temperature value you wish to convert: '))
        A = UserTemp
        convertedTemp = A + C
        print(convertedTemp)
        
        break
    
    elif Convert == 'K-C':
        UserTemp = float(input('Enter the temperature value you wish to convert: '))
        A = UserTemp
        convertedTemp = A - C
        print(convertedTemp)
        
    
        break
