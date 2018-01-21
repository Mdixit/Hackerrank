#method 1 but very slow.

def main():
    #import pdb; pdb.set_trace()
    a = input()
    b = input()
    res = calc_fun(a,b)
    print(res)

def calc_fun(a,b):
    sum = 0
    init_b = len(b)
    if len(a) >= len(b):
        l = len(b)
    else:
        l = len(a)
    for i in range(l+1):
        x = int(a,2) ^ int(b,2)
        sum += x
        sum = sum % 1000000007
        b = str(bin(int(b,2) << 1))

    binx = str(bin(x))
    front =  binx[2:2+init_b]
    back = binx[2+init_b:]
    for j in range(314159 - (l)):
        front = front + '0'
        numb = front + back
        num = int(numb,2)
        sum += num
        sum = sum % 1000000007
        print(j)
    return sum

if __name__ == '__main__':
    main()
