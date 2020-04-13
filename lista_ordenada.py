def ordenada(lista):
    if len(lista)==1:
        return True 
    
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[j] < lista[j-1]:
                return False
        return True
    


