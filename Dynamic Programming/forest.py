def calc_val(iput):
    
    s=1
    init_val = fin_val =sum(iput)
   # iput = sorted(iput)
    for j in range(1,len(iput)):
        k = min(iput)
        s = s + 1
        new_sum = init_val - k
        fin_val = max(fin_val,s*new_sum)
        init_val = new_sum
        if(fin_val > s*new_sum):
            break
        iput.remove(k)
       # print(k)
       # print(fin_val)
    
    return fin_val

def main():
    t_case = input()
    t_case = int(t_case)
    inp_lst = []
    tmp_ar = []
    for j in range(t_case):
        leng = input()
    
    
        tmp = input()
        tmp_ar = tmp.split()
        tmp_ar = [int(l) for l in tmp_ar]
        inp_lst.append(tmp_ar)
        tmp_ar = []
    for t in inp_lst:
        val = calc_val(t)
        print(val)

if __name__ == "__main__":
    main()
