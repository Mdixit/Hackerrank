def calc_val(iput):
    if(len(iput)==1):
        return 0
    pt = 0   
    sum_l = iput[0]
    sum_r = sum(iput[1:])
    
    for j in range(1, len(iput)):
        if(j ==0):
            continue
        if(sum_l == sum_r):
            pt = 1 + max(calc_val(iput[j:]),calc_val(iput[:j]))
            break
        if(sum_l != sum_r):
        
            sum_l += iput[j]
            sum_r -= iput[j]
            
    return pt

def main():
    t_case = input()
    t_case = int(t_case)
    listolist = []
    pnt = []
    for j in range(t_case):
        size = input()
        size = int(size)
        inp = input()
        list1 = inp.split()
        list1 = [int(e) for e in list1]
        listolist.append(list1)      
        list1 = []
    
    for j in listolist:
        if(sum(j)==0):
            pnt.append(len(j)-1)
        else:
            pnt.append(calc_val(j))
    
    for k in pnt:
        print(k)

if __name__ == "__main__":
    main()
