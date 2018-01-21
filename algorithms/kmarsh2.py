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
        for j in range(len(inpu[i])):
            if inpu[i][j] == '.':
                left[i][j] = cnt
                cnt = cnt + 1
            else:
                left[i][j] = -1
                cnt = 0
    #calc up matrix

    for l in range(len(inpu)):
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
    maxprem = 0
    for i in range(1,len(inpu)):
        for j in range(1,len(inpu[1])):
            upval = up[i][j]
            leftval = left[i][j]
            flag = 0
                
