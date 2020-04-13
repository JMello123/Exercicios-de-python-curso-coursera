def maiusculas(frase):
    letrasMai = ""
    pos = 0
    while pos <= len(frase) - 1:
        if ord(frase[pos]) < 91 and ord(frase[pos]) >= 65:
            letrasMai = letrasMai + frase[pos]
        pos = pos + 1 
    return letrasMai

maiusculas('oi, Daniela e David')