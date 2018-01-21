def calc_val(iput):   #only passes half testcases

    prt_ar = []
    tmp_lst = []
    wt = []
    for j in range(len(iput)-1):
        
        if(iput[j] < iput[j+1]):
            tmp_lst.append(iput[j])
            
        else:
            tmp_lst.append(iput[j])
            prt_ar.append(tmp_lst)
            tmp_lst = []
            wt.append(0)

    if(tmp_lst != []):
        prt_ar.append(tmp_lst)
    
    if(iput[-1] > iput[-2]):
        prt_ar[-1].append(iput[-1])
        wt.append(0)
    else:
        prt_ar.append([iput[-1]])
        wt.append(0)
    flag = 1
    
 
    
    for k in reversed(range(len(prt_ar))):
        
        if(flag == 1):
            if(len(prt_ar[k]) == 1):
                wt[k] = 1
                flag = 0
                continue
            else:
                wt[k] = (len(prt_ar[k]) * (len(prt_ar[k])+1))/2
                flag = 0
                continue
        
        if(len(prt_ar[k]) != 1 and len(prt_ar[k+1]) != 1 ):
            wt[k] = (len(prt_ar[k]) * (len(prt_ar[k])+1)) / 2

        elif(len(prt_ar[k]) != 1 and len(prt_ar[k+1]) == 1):
            if(len(prt_ar[k])-wt[k+1] <= 0 ):
                wt[k] = ((len(prt_ar[k]) * (len(prt_ar[k])+1)) / 2) - len(prt_ar[k]) + wt[k+1] + 1     
                
            else:
                wt[k] = ((len(prt_ar[k]) * (len(prt_ar[k])+1)) / 2)

        elif (len(prt_ar[k]) == 1 and len(prt_ar[k+1]) != 1):
            if(prt_ar[k][0] > prt_ar[k+1][0]):
                wt[k] = 2
            else:
                wt[k] = 1
        elif (len(prt_ar[k]) == 1 and len(prt_ar[k+1]) == 1 ):
            if(prt_ar[k] > prt_ar[k+1]):
                wt[k] = wt[k+1] + 1
            else:
                wt[k] = 1

    print(prt_ar)
    print(wt)
    return sum(wt)

def main():
    num = input()
    num = int(num)
    li = []
    for k in range(num):
        tmp = input()
        li.append(int(tmp))
    val = calc_val(li)
    print(int(val))
if __name__ == "__main__":
    main()
            
        
                

