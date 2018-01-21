#Too slow after input 10^6
import math;
arry = []
vals = []
arry.append(0)
arry.append(1)
vals.append([0])
vals.append([1])
global i
i = 2
prev = []
prev = [1]
def main():
    t = int(input())
    ar = []
    for x in range(t):
        b = int(input())
        if b < len(arry):
            print(arry[b-1])
            continue
        else:
            res = calc_val(b)



def calc_val(q):
    #import pdb; pdb.set_trace()
    global i
    global arry
    global prev
    flag = 0
    new = []
    new2 = []
    while flag == 0:
        if (len(arry)) >= q:
            #print(arry)
            #print(vals)
            print(arry[q-1])
            flag = 1
            continue
        if i % 2 == 0:
            for j in prev:
                if(j % 10 == 9):
                    continue
                new.append(j+1)
            for k in vals[int(i/2)]:
                new2.append(k*10)
            x = 0
            #import pdb; pdb.set_trace()
            tmp = []
            while len(new) > 0 and len(new2)> 0:
                if(new[0] > new2[0]): tmp.append(new2.pop(0))
                else : tmp.append(new.pop(0))
            tmp.extend(new + new2)
            new = tmp
        if i % 2 == 1 :
            for j in prev:
                if(j % 10 == 9):
                    continue
                new.append(j+1)
        arry = arry + new
        vals.append(new)
        prev = new
        new = []
        new2 = []
        i = i+1
if __name__=="__main__":
    main()
