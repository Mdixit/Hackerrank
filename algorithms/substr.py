def func(iplst):  #right solution but timed out and gave segmentation error for few test cases.
    tab = [[]]
    templst = []
    temp = 0
    tot = 0
    tab[0] = iplst
    for i in range(2,(len(iplst)+1)):
        for j in range(1,(len(iplst)+2)-i):
            temp = tab[i-2][j-1] * 10
            temp += iplst[j+i-2]
            templst.append(temp)
            
        tab.append(templst)
        templst = []
    for k in range(len(tab)):
        tot += sum(tab[k])
    return tot    

def main():
    iput = input()
    iput = int(iput) 
    iplst = []
    while iput > 0:
        tmp = iput%10
        iplst.append(tmp)
        iput = iput/10

    iplst.reverse()
    
    k = func(iplst)    
    ans = k % (1000000007)
    print (ans)

if __name__=="__main__":
    main()
