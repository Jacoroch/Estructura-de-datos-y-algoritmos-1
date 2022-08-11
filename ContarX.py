def contarX(str):
    print (str)
    
    if len(str) == 0:
        return 0
    elif str[0] == "x":    
        return 1 + contarX(str[1:])
    else    : 
        return contarX(str[1:])

str = input("ingrese la cadena de texto: ")
print(contarX(str))
