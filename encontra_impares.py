def encontra_impares(lista):
    impares = []
    if len(lista) > 0:
        numero = lista.pop(0)
        if numero%2 == 1:
            impares.append(numero)

        impares = impares + encontra_impares(lista) 
    return impares
