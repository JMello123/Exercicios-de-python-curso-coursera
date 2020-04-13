def busca(lista,elemento):
    ponto_inicio = 0 
    ponto_final = len(lista)-1

    while ponto_inicio <= ponto_final:
        ponto_medio = (ponto_inicio + ponto_final) // 2
        
        if lista[ponto_medio] == elemento:
            print(ponto_medio)
            return ponto_medio

        else:
            if  elemento < lista[ponto_medio]:
                ponto_final = ponto_medio - 1
                print(ponto_medio)
            else:
                ponto_inicio = ponto_medio + 1
                print(ponto_medio)
      
    return False


#a = busca([1, 2, 3, 4, 5, 6],4)
#a = busca([1,2,3,4,5], 6)
