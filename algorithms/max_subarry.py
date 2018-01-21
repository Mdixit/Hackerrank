import sys

def calc_val(Listt):
    alneg = 1
    alpos = 1
    alzer = 1
        
    for j in Listt:
        if (j>0):
            alneg = 0
            break
        
    for k in Listt:
         if (k<0):
            alpos = 0
            break
        
    for l in Listt:
        if (l!=0):
            alzer = 0
            break

    if(alneg == 1):
        print(max(Listt), max(Listt))

    elif(alpos == 1):
        print(sum(Listt), sum(Listt))
        
    elif(alzer == 1):
        print(0, 0)

    elif(len(Listt) == 2 ):
        print(max(Listt), max(Listt))
    else:
        nconti = 0
        max_h = max_so = Listt[0]
        for j in Listt[1:]:
            max_h = max(j,max_h+j)
            max_so = max(max_h,max_so)
            if(j>0):
                nconti += j    
        if(Listt[0]>0):
            nconti += Listt[0]
        print(max_so, nconti)

def main():
    t_case = input()
    t_case = int(t_case)
    listolist = []
    for i in range(t_case):
        size = input()
        inp = input()
        list1 = inp.split()
        list1 = [int(e) for e in list1]
        listolist.append(list1)      
        list1 = []

    for j in range(len(listolist)):
        calc_val(listolist[j])

if __name__ =="__main__":
    main()

        











            









