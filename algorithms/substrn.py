def func(iput): #correct soln
    mulpler = 0
    sumf = 0
    
    for i in range(len(iput)):
        
        mulpler = ((mulpler * 10) + 1)
        mulpler = mulpler % 1000000007
        sumf = sumf + (iput[(len(iput))-i-1] * mulpler * (len(iput)-i))
        sumf = sumf % 1000000007
    return sumf

def main():
    inp = input()
    iputm = []
    iputm = [int(x) for x in str(inp)]
    fin = func(iputm)
    print(fin)

if __name__=="__main__":
    main()
    
