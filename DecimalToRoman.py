
def convert_decimal_to_roman(decimal_number):
    resto = decimal_number % 10
    resto_entero = decimal_number // 10
    rto_1 = ""
    rto = ""
    if resto_entero != 0:
        if resto_entero == 1:
            rto = "X"
        if resto_entero == 2:
            rto = "XX"
        if resto_entero == 3:
            rto = "XXX"
        if resto_entero == 4:
            rto = "XL"
        if resto_entero == 5:
            rto = "L"
        if resto_entero == 6:
            rto = "LX"
        if resto_entero == 7:
            rto = "LXX"
        if resto_entero == 8:
            rto = "LXXX"
        if resto_entero == 9:
            rto = "XC"
        if resto_entero == 10:
            rto = "C"
    if resto == 0 and decimal_number > 10:
        if decimal_number == 10:
            rto = "X"
        if decimal_number == 20:
            rto = "XX"
        if decimal_number == 30:
            rto = "XXX"
        if decimal_number == 40:
            rto = "XL"
        if decimal_number == 50:
            rto = "L"
        if decimal_number == 60:
            rto = "LX"
        if decimal_number == 70:
            rto = "LXX"
        if decimal_number == 80:
            rto = "LXXX"
        if decimal_number == 90:
            rto = "XC"
        if decimal_number == 100:
            rto = "C"
    elif resto_entero != 0 or resto_entero == 0:
        if decimal_number == 1 or resto == 1:
            rto_1 = "I"
        if decimal_number == 2 or resto == 2:
            rto_1 = "II"
        if decimal_number == 3 or resto == 3:
            rto_1 = "III"
        if decimal_number == 4 or resto == 4:
            rto_1 = "IV"
        if decimal_number == 5 or resto == 5:
            rto_1 = "V"
        if decimal_number == 6 or resto == 6:
            rto_1 = "VI"
        if decimal_number == 7 or resto == 7:
            rto_1 = "VII"
        if decimal_number == 8 or resto == 8:
            rto_1 = "VIII"
        if decimal_number == 9 or resto == 9:
            rto_1 = "IX"
    return rto + rto_1
