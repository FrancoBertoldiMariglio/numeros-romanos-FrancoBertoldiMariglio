
valores = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    }


def conversion_romano_to_numero(romano):
    sum = 0
    for i in range(len(romano) - 1):
        left = romano[i]
        right = romano[i + 1]
        if valores[left] < valores[right]:
            sum -= valores[left]
        else:
            sum += valores[left]
    sum += valores[romano[-1]]
    return sum
