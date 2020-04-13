def menor_nome(nomes):
    nomesTratados = []
    menor = []
    for palavra in nomes:
        palavraTratada = palavra.strip().capitalize()# retira os espaços e capitaliza cada palavra
        nomesTratados.append(palavraTratada)
        menor.append(len(palavraTratada))#insere o comprimento da palavraTratada na lista menor

    posMenor = menor.index(min(menor))#busca o index do menor valor presente na lista menor
    palavraMenor = nomesTratados[posMenor]
            
    print(palavraMenor)

menor_nome(['zé', ' lu', 'fê'])