import pdb
def main():
    t = int(input())
    arrb =[]
    for x in range(t):
        size = input()
        b = input()
        b = b.split()
        temp = [int(e) for e in b]

        arrb.append(temp)

    for y in range(len(arrb)):
        result = calc_cost(arrb[y])
        print(result)

def calc_cost(arr):
    h = 0
    l = 0
    hi = 0
    low = 0


    for i in range(1,len(arr)):
        l = max(low,abs(hi+(arr[i-1]-1)))
        h = abs(low + arr[i]-1)

        hi = h
        low = l
    return max(hi,low)

if __name__=="__main__":
    main()
