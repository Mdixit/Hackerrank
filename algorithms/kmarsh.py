def main():
    t = input()
    m_n = t.split()
    m = int(m_n[0])
    n = int(m_n[1])
    inp = []
    for i in range(m):
        temp = input()
        inp.append(list(temp))

    res =  calc_val(inp)
    if res == 0:
        print('impossible')
    else:
        print(res)

def calc_val(inpu):
        #calc left matrix

    left =[[0]*len(inpu[1]) for _ in range(len(inpu))]
    up = [[0]*len(inpu[1]) for _ in range(len(inpu))]
    for i in range(len(inpu)):
        cnt = 0
        for j in range(len(inpu[1])):
            if inpu[i][j] == '.':
                #print(i,j)
                left[i][j] = cnt
                cnt = cnt + 1
            else:
                left[i][j] = -1
                cnt = 0
    #calc up matrix
    for l in range(len(inpu[1])):
        if inpu[0][l] == '.':
            up[0][l] = 0
        else:
            up[0][l] = -1
    for j in range(1,len(inpu)):
        for k in range(len(inpu[i])):
            if inpu[j][k] =='.':
                up[j][k] = up[j-1][k] + 1
            else:
                up[j][k] = -1
    #print(left)
    #print(up)
    dp = [[0]*len(inpu[1]) for _ in range(len(inpu))]
    #import pdb; pdb.set_trace()
    maxprem = 0
    for i in range(1,len(inpu)):
        for j in range(1,len(inpu[1])):
            upval = up[i][j]
            leftval = left[i][j]
            flag = 0

            if upval == 0 or leftval == 0 or upval == -1 or leftval == -1:
                dp[i][j] = 0
                continue
            if maxprem > 2*(upval + leftval):

                continue


            while flag == 0:
                #print(dp)
                if upval == 0 or leftval == 0 :
                    flag = 1
                    continue

                if maxprem > 2*(upval + leftval):
                    flag = 1
                    continue
                up_left = left[i-upval][j]
                #print(i,j,leftval)
                left_up = up[i][j-leftval]
                if up_left == 0 or up_left == -1:
                    upval = upval -1
                    continue

                if left_up == 0 or left_up == -1:
                    leftval = leftval - 1
                    continue
                if up_left >= leftval and left_up >= upval:
                    dp[i][j] = 2*(leftval + upval)
                    flag = 1
                    if maxprem < dp[i][j]:
                        maxprem = dp[i][j]
                    continue
                if up_left >= leftval and left_up <= upval:
                    #upval = upval - 1
                    temp_val = leftval -1
                    while temp_val > 0:
                        if up[i][j-temp_val] >= upval:
                            prem = 2 * (upval + temp_val)
                            if prem > dp[i][j]:
                                dp[i][j] = prem
                            if maxprem < dp[i][j]:
                                maxprem = dp[i][j]
                            break
                        else:
                            temp_val = temp_val - 1
                    upval = upval - 1
                    continue
                if up_left <= leftval and left_up >= upval:
                    temp_val = upval - 1
                    while temp_val > 0:
                        if up[i-temp_val][j] >= leftval:
                            prem = 2 * (leftval + temp_val)
                            if prem > dp[i][j]:
                                dp[i][j] = prem
                            if maxprem < dp[i][j]:
                                maxprem = dp[i][j]
                            break
                        else:
                            temp_val = temp_val - 1
                    leftval = leftval - 1
                    continue
                if up_left < leftval and left_up < upval:
                    temp_left = up_left
                    temp_up = left_up
                    while temp_left > 0:
                        if up[i][j-temp_left] >= upval:
                            prem = 2 * (upval + temp_left)
                            if prem > dp[i][j]:
                                dp[i][j] = prem
                            if maxprem < dp[i][j]:
                                maxprem = dp[i][j]
                            break
                        else:
                            temp_left = temp_left - 1
                    while temp_up > 0:
                        if left[i-temp_up][j] >= leftval:
                            prem2 = 2 * (leftval + temp_up)
                            if prem2 > dp[i][j]:
                                dp[i][j] = prem2
                                if maxprem < dp[i][j]:
                                    maxprem = dp[i][j]
                            break
                        else:
                            temp_up = temp_up - 1
                    upval = upval - 1
                    leftval = leftval - 1

                    continue
    #print(dp)
    return maxprem
if __name__ == "__main__":
    main()
