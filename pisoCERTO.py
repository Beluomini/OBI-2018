def main():
    largura = int(input())
    comprimento = int(input())
    l2 = 0
    l3 = 0
    l2 = (comprimento-1)*2 +(largura-1)*2
    l3 = comprimento*largura + (comprimento-1) * (largura-1)
    print(l3)
    print(l2)
    
