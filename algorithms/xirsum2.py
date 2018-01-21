def main():
    #import pdb; pdb.set_trace()
    a = input()
    b = input()
    res = calc_fun(a,b)
    print(res)
def calc_fun(a,b):
    #pad a to 314160 bits
    #import pdb; pdb.set_trace()
    dp = [0 for _ in range(314160 + len(b))]
    inv_dp = [0 for _ in range(314160 + len(b))]
    #initialise dp for base case
    if a[-1] == '0' and b[-1] == '0' or a[-1] == '1' and b[-1] == '0' :
        dp[0] = 0
        #inv_dp[0] = 10
        inv_dp[0] = 314160

    if a[-1] == '1' and b[-1] == '1' or a[-1] == '0' and b[-1] == '1':
        dp[0] = 1
        #inv_dp[0] = 9
        inv_dp[0] = 314159
    if a[-1] == '0':
        ones = dp[0]
    else:
        ones = inv_dp[0]
    power = 1
    finans = ones
    #print(ones)
    def getxor(j):
        if j > len(b):
            if a[-j] == '1':
                return 1
            else:
                return 0
        else:
            if a[-j] == '0' and b[-j] == '1' or a[-j] == '1' and b[-j] == '0' :
                return 1
            else :
                return 0
    for i in range(2,314159 + len(b)+1):

        if i > len(a):
            a = '0' + a
        bit = getxor(i)
        if i > 314160:
            #import pdb; pdb.set_trace()
            offset = i - 314160
            dpoff = dp[offset-1]
            inv_dpoff = inv_dp[offset-1]
        else:
            dpoff = 0
            inv_dpoff = 0
        if bit == 1:
            if a[-i] == '0':
                dp[i-1] = dp[i-2] + 1
                inv_dp[i-1] = inv_dp[i-2] - 1
                ones = dp[i-1] - dpoff
            else:
                dp[i-1] = dp[i-2]
                inv_dp[i-1] = inv_dp[i-2]
                ones = inv_dp[i-1] - inv_dpoff
        if bit == 0:
            if a[-i] == '0':
                dp[i-1] = dp[i-2]
                inv_dp[i-1] = inv_dp[i-2]
                ones = dp[i-1]  - dpoff
            else:
                inv_dp[i-1] = inv_dp[i-2] - 1
                dp[i-1] = dp[i-2] + 1
                ones = inv_dp[i-1] - inv_dpoff
        #print(dp[i-1])
        #print(inv_dp[i-1])
        #print(ones)
        power = (power * 2) % 1000000007
        ans = ( power * ones ) % 1000000007
        #print(ans)
        #q = input()
        finans = (ans + finans) % 1000000007


    return finans
if __name__ == '__main__':
    main()
