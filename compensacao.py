def main():
    teste = 0
    resposta = ""
    l1 = input()
    lx = ""
    l1a = l1.split(" ")
    numcheques = int(l1a[0])
    numcidadaos = int(l1a[1])
    ldevedores = [0]*(numcheques+1)
    lreceptores = [0]*(numcheques+1)
    if numcheques <= 2:
        resposta = "N"
    else:
        for i in range(1, numcidadaos+1):
            lx = input()
            lxa = lx.split(" ")
            ldevedores[i] = int(lxa[0])
            lreceptores[i] = int(lxa[2])
        for a in range(0,numcheques-1):
            for t in range(0,numcheques-1):
                if ldevedores[a]==ldevedores[t]:
                    teste+=1
        if teste>= 6:
            resposta = "S"
        else:
            resposta = "N"
