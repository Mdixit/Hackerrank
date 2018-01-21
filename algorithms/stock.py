def calc_val(stock):
    s_val = 0
    if(len(stock) == 1):
        return 0
    max_val = max(stock)
    idx = stock.index(max_val)
    if(idx == len(stock)-1):
        return ((idx*max_val)-sum(stock[:idx]))
    s_val = ((idx * max_val)-sum(stock[:idx])) + calc_val(stock[idx+1:])
    return s_val

def main():
    t_case = input()
    t_case = int(t_case)
    fin_ar = []
    for k in range(t_case):
        day = input()
        day = int(day)
        stocp = input()
        sto_ar = stocp.split()
        sto_ar =[int(k) for k in sto_ar]
        fin_ar.append(sto_ar)
        sto_ar = []
    for j in fin_ar:
        val = calc_val(j)
        print(val)
if __name__ == "__main__":
    main()
