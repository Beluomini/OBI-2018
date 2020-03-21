def main():
    l1 = input()
    l2 = input()
    l3 = input()
    l1a = l1.split(" ")
    nfigurinhas = int(l1a[0])
    nfigurinhasdouradas = int(l1a[1])
    nfigurinhascompradas = int(l1a[2])
    figurinhasdouradas = l2.split(" ")
    figurinhascompradas = l3.split(" ")
    figqfaltam = nfigurinhasdouradas
    for x in range(0,nfigurinhascompradas):
        a=0
        for i in range(0,nfigurinhascompradas):
            if figurinhascompradas[x] == figurinhascompradas[i]:
                a+=1
                if a>1:
                    figurinhascompradas[i] = 0
    for i in range(0,nfigurinhascompradas):
        for a in range(0,nfigurinhasdouradas):
            if figurinhascompradas[i] == figurinhasdouradas[a]:
                figqfaltam=figqfaltam-1
    print(figqfaltam)
        
    
    
