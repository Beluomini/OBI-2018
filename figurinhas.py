def main():
    l1 = input()
    l2 = input()
    l3 = input()
    l1a = l1.split(" ")
    l2a = l2.split(" ")
    l3a = l3.split(" ")
    nfa = int(l1a[0])
    nfc = int(l1a[1])
    nfcom = int(l1a[2])
    figc = [0]*nfc
    figcom = [0]*nfcom
    figqf = nfc
    for i in range(0,nfc):
        f = l2a[i]
        figc [i] = f
    for x in range(0,nfcom):
        g = l3a[x]
        figcom [x] = g
        for t in range(0,nfc):
            if g == figc[t]:
                figqf = figqf-1
    print(figqf)
                
    
        
    
    
