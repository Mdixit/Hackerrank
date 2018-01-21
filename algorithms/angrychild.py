def main(): #times out in most of cases
    pac = int(input())
    chd = int(input())
    ilst = []
    for i in range(pac):
        tmp  = int(input())
        ilst.append(tmp)

    ilst.sort()
    wtlst = []
    wt = 0
    temp = 0
    for j in reversed(range(1,chd)):
        for k in range(j):
            wt += abs(ilst[j] - ilst[k])

    wtlst.append(wt)

    for l in range(1,len(ilst)-chd+1):
        tem = wtlst[l-1]
        temp2 =  ((chd-1)*ilst[l+chd-1])
        wtlstt = tem + temp2
        
        for m in range(2,chd+1):
            temp += ilst[l+m-2] 
        temp = (2*temp) - (chd-1)*ilst[l-1]
        wtlst.append(abs(wtlstt - temp))
        temp = 0
    
    ans = min(wtlst)
    print (ans)

if __name__=="__main__":
    main()
