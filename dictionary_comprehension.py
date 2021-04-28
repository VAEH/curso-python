#Generación de llaves con los 100 primeros número en naturales y sus valores elevados al cuadrado


def run():
    """
    my_dict={}

    for i in range(1,101):
        if i %3 !=0:
            my_dict[i]= i**3
    print(my_dict)
    """
    #Es algo diferente al de List Comprehension, debido a que señala al inicio el valor de la llave "i"
    # y luego, el de su correspondiente valor  
    #my_dict = {i:i **3 for i in range(1, 101) if i%3 !=0}

    
    #Desafio consiste hacer un diccionario comprehesion, 
    # donde las llaves sean los 1000 primeros numeros naturales con sus raices cuadradas como valor
    my_dictionary = {i:i**(1/2) for i in range(1, 1001) }
    print(my_dictionary)

if __name__ == "__main__":
    run()
