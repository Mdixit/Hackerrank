
def count(amount,n,denom):
    
    sumlst = []
    temp_lst = []
    denom.sort()
    mi =  denom.pop(0)
    for i in range(amount+1):
    
        if i % mi == 0 :
            temp_lst.append(1)

        else:
            temp_lst.append(0)
    sumlst.append(temp_lst)
    
    for de in denom:
        temp_lst = []
        for k in range(amount+1):
            if k < de :
                temp_lst.append(sumlst[0][k])
            else:
                val =  sumlst[0][k] + temp_lst[k-de]
                temp_lst.append(val)
                    
        sumlst = []
        sumlst.append(temp_lst)
    print(sumlst[0][-1])
    
def main():
    amt = input()
    temp = amt.split()
    amt =int(temp[0])
    coin = int(temp[1])
    denom = []
    tmp = input()
    denom = tmp.split()
    denom = [int(l) for l in denom]
    count(amt,coin,denom)

if __name__ == "__main__" :
    main()
