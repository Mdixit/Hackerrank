def calc_val(a,b):

    dp = [[0 for m in range(len(a))] for i in range(len(b))]
    cnt = 1
    capsflag = 0

    p = b[0]

    for r in range(len(a)):
        if p == a[r]:
            if capsflag == 1 :
                dp[0][r] =  0

            if capsflag == 0:
                dp[0][r] = 1
                capsflag = 1

        elif p == a[r].upper():
            if r > 0 and capsflag == 0:
                dp[0][r] = 1
            else:
                dp[0][0] = 1
        else:
            if a[r].islower():
                if r > 0:
                    dp[0][r] = dp[0][r-1]
                else:
                    dp[0][0] = 0
            else:
                dp[0][r] = 0
                capsflag = 1

    for y in range(1,len(b)):
        capsflag = 0
        for x in range(cnt,len(a)):
            if a[x] == b[y]:
                #    if capsflag == 1 :
                #        dp[y][x] =  0

                #    if capsflag == 0:
                    dp[y][x] = dp[y-1][x-1]
                        #if dp[y][x] == 1:
                #            capsflag = 1

            elif b[y] == a[x].upper():
                if dp[y-1][x-1] == 1 or dp[y][x-1]==1:
                    dp[y][x] = 1
                else:
                    dp[y][x] = 0
            else:
                if a[x].islower():
                    dp[y][x] = dp[y][x-1]
                else:
                    dp[y][x] = 0


        cnt = cnt + 1
        #if cnt == 10:
        #    import pdb; pdb.set_trace()
    #j = []
    #count = 0
    #for j in dp:
    #    if sum(j) == 0:
    #        print(count)
    #    count = count + 1
    #print(dp)
    j = []
    j = dp.pop()
    #print(j)
    if j[len(a)-1] == 1:
        return ('YES')

    else:
        return ('NO')
    return
def main():
    ans = []
    t = int(input())
    for j in range(t):
        #import pdb; pdb.set_trace()
        A = input()
        B = input()
        A = list(A)
        B = list(B)
        a = calc_val(A,B)
        ans.append(a)
        print (ans)
if __name__ == '__main__':
    main()
