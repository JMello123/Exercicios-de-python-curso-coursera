def soma_matrizes (m1,m2):
    linha_m1 = len(m1)
    coluna_m1 = len(m1 [0])
    linha_m2 = len(m2)
    coluna_m2 = len(m2 [0])
    matriz_soma = []

    if linha_m1 == linha_m2 and coluna_m1 == coluna_m2:
        for i in range(linha_m1):
            linha = []
            for j in range(coluna_m1):
                valor = m1[i][j] + m2[i][j]
                linha.append(valor)
            matriz_soma.append(linha)
        return matriz_soma
    else:
        return False 

m1 = [[2]]
m2 = [[2]]
soma_matrizes(m1, m2)