
def binaire_decimal(binaire):
    decimal = 0 
    binaire = str(binaire)[::-1]
    
    for i in range(len(binaire)):
        if binaire[i] == '1':
            decimal += 2**i
    return decimal 


code = '1111'
print(f'Le binaire {code} converti en manuellement donne : {binaire_decimal(code)}')


