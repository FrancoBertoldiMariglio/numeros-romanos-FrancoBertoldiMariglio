""" def conversion_romano_to_numero(romano):
    for x in romano:
        lista_decimal = []
        if x == "I":
            letra_1 = 1
            lista_decimal.append(letra_1)
        if x == "V":
            letra_2 = 5
            lista_decimal.append(letra_2)
        if x == "X":
            letra_3 = 10
            lista_decimal.append(letra_3)
        if x == "L":
            letra_4 = 50
            lista_decimal.append(letra_4)
        if x == "C":
            letra_5 = 100
            lista_decimal.append(letra_5)

    for i in range(0, len(lista_decimal)):
        if i == 0:
            if conversion_romano_to_numero(i) >= conversion_romano_to_numero(
                    i + 1):
                a = conversion_romano_to_numero(
                    i + 1) - conversion_romano_to_numero(i)
            if conversion_romano_to_numero(i) < conversion_romano_to_numero(i +
                                                                            1):
                a = conversion_romano_to_numero(
                    i) + conversion_romano_to_numero(i + 1)
        else:
            if a >= conversion_romano_to_numero(i + 1):
                a = +-conversion_romano_to_numero(i)
            if a < conversion_romano_to_numero(i + 1):
                a = +conversion_romano_to_numero(i + 1)
 """

def conversion_romano_to_numero(romano):
    
    lista_decimal = []
    letra_1 = 1
    letra_2 = 5
    letra_3 = 10
    letra_4 = 50
    letra_5 = 100
    acumulador = 0
    
    for x in romano:
    
        if x == "I":
            lista_decimal.append(letra_1)
        if x == "V":
            lista_decimal.append(letra_2)
        if x == "X":
            lista_decimal.append(letra_3)
        if x == "L":
            lista_decimal.append(letra_4)
        if x == "C":
            lista_decimal.append(letra_5)
    
    for i in lista_decimal:
        acumulador = acumulador + i
    
    return acumulador