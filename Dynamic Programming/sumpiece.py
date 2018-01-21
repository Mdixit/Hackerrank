import sys
def sumcalc(iput,n):
    
    coeff = []
    multi = []
    temp = pow(2,n,1000000007) - 1 
    coeff.append(temp)
    if (n%2) == 0 :                   
        k = n/2
        k = int(k)
    else:
        k = (n + 1) / 2
        k = int(k)
    for j in range(1,k+1):
        nxtval = (coeff[j-1] + pow(2,(n-2)-(j-1),1000000007) - pow(2,j-1,1000000007)) % ((pow(10,9) + 7 ))
        coeff.append(nxtval)
        nxtval = 0
    multi = []
    diff = n-1
    for l in range(0,k):
        tem = (iput[l] * coeff[l]) % (pow(10,9) + 7 )
        multi.append(tem)    
        if diff > l:
        
            tem = (iput[diff] * coeff[l]) %  (pow(10,9) + 7 )
            multi.append(tem)

        diff = diff - 1   
    finval = sum(multi) % (pow(10,9) + 7 )
    print(finval)

def main():
    lth = int(sys.stdin.readline())
    tm = input()
    iput = []
    t_iput = tm.split()
    iput = [int(l)  for l in t_iput]
    sumcalc(iput,lth)

if __name__ == "__main__" :
    main()
