import compensacao
import compensacaoCERTO
import figurinhas
import figurinhasCERTO
import piso
import pisoCERTO
def main():
    print('------------MENU----------')
    print('1 ---------- respostas Lucas')
    print('2 ---------- Gabarito')
    menu1 = int(input("Digite sua Opção: "))
    menu2 = 0=
    if(menu1 == 1):
        print('------------EXERCÍCIO----------')
        print('1 ---------- Compensação')
        print('2 ---------- Figurinhas')
        menu2 = int(input("Digite sua Opção: "))
        if(menu2 == 1):
            compensacao.main()
        elif(menu2 == 2):
            figurinhas.main()
    elif(menu1 == 2):
        print('------------EXERCÍCIO----------')
        print('1 ---------- Compensação')
        print('2 ---------- Figurinhas')
        print('3 ---------- Piso')
        menu2 = int(input("Digite sua Opção: "))
        if(menu2 == 1):
            compensacaoCERTO.main()
        elif(menu2 == 2):
            figurinhasCERTO.main()
        elif(menu2 == 3):
            pisoCERTO.main()