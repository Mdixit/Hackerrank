import pdb;
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

        result = calc_val(arrb[y])
        print(result)


def calc_val(arval):
    prime = [1 for _ in range(8193)]
    prime[0] = 0
    prime[1] = 0
    for k in range(2,4096):
        if prime[k]:
            y = k * 2
        while  y < 8193:
            prime[y] = 0
            y = y + k

    res = 0
    cnt = []
    cnt = [ 0 for _ in range(1000)]
    for l in arval:
        cnt[l-3500] += 1
    arval = list(set(arval)) #unique elements only
    n = len(arval)

    dp = [[0]*8192 for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(1,n+1):
        for j in range(8192):

            dp[i][j] = dp[i-1][j] * int((cnt[arval[i-1]-3500] + 2)/2) + dp[i-1][j ^ arval[i-1]] * int((cnt[arval[i-1]-3500] + 1)/2)
            dp[i][j] = dp[i][j] % 1000000007
    for m in range(8192):

        if prime[m] == 1:

            res += dp[n][m]
            res = res % 1000000007
    return(res)

if __name__=="__main__":
    main()
