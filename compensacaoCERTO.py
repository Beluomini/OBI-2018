def main():
    teste = 0
    resposta = ""
    resposta2 = 0
    linha = ""
    l1 = input()
    l1a = l1.split(" ")
    numcheques = int(l1a[0])
    numcidadaos = int(l1a[1])
    ldevedores = [0]* numcheques
    lreceptores = [0]* numcheques
    valorescheques = [0]* numcheques
    cidadaos = [0] * numcidadaos
    saldo = [0] * (numcidadaos+1)
    for x in range(0,numcidadaos):
        cidadaos[x] = x
    if numcheques <= 2:
        resposta = "N"
    else:
        for i in range(0, numcheques):
            linha = input()
            linha1 = linha.split(" ")
            ldevedores[i] = int(linha1[0])
            valorescheques[i] = int(linha1[1])
            lreceptores[i] = int(linha1[2])
            saldo[int(linha1[0])] = saldo[int(linha1[0])] - int(linha1[1])
            saldo[int(linha1[2])] = saldo[int(linha1[2])] + int(linha1[1])
        for a in range(0,numcheques):
            for t in range(0,numcheques):
                if ldevedores[a]==lreceptores[t]:
                    teste+=1
        for f in range(0,numcidadaos):
            if saldo[f] >= 0:
                resposta2 += saldo[f]
        if teste>= 1:
            resposta = "S"
            print(resposta)
            print(resposta2)
        else:
            resposta = "N"
            print(resposta)
