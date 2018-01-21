def main():
    t_case = int(input())
    for i in range(t_case):
        line = []
        line = input().split()
        city = int(line[0])
        road = int(line[1])
        clib = int(line[2])
        croad = int(line[3])
        #import pdb; pdb.set_trace()
        path = {k : [] for k in range(1,city+1)}
        for i in range(road):
            to_fr = []
            to_fr = input().split()
            to = int(to_fr[1])
            frm = int(to_fr[0])

            #if not(frm in path):
            #    path[frm] = []

            #if not(to in path):
            #    path[to] = []

            path[frm].append(to)
            path[to].append(frm)
        cost = calc_cost(path,city,clib,croad)
        print(cost)
        #print(path)
def calc_cost(path,city,clib,croad):
    #import pdb; pdb.set_trace()
    comp_flag = 1
    result = 0
    comp_len = 0        #length of connected component
    prev_len = 0
    visited = {}
    temp = 0
    remotenode = 0
    #kl = list(path)
    stack = []
    #stack.append(kl[0])
    #visited = {kl[0]:1}
    #nextnode = path[kl[0]]
    while (len(visited) != city):
        for j in path:
            if path[j] == [] and j not in visited:
                remotenode += 1
                visited[j] = 1
                prev_len += 1
                continue
            if (j not in visited):
                stack.append(j)

                break
        while(stack != []): #fix
            comp_flag = 0
            nextnode = stack.pop()
            if nextnode not in visited:
                visited[nextnode] = 1
                try:
                    for i in path[nextnode]:
                        if i not in visited and i not in stack:
                            stack.append(i)
                            #print(stack)
                except Exception as e:
                    pass
                #for i in path[nextnode]:
                #    if i not in visited:
                #        stack.append(i)
                #        print(stack)
        if comp_flag == 0:
            #import pdb; pdb.set_trace()
            comp_len = len(visited) - prev_len
            prev_len += comp_len
            temp = min(clib + ((comp_len-1)*croad),comp_len*clib)
            result += temp
            comp_flag = 1
    if remotenode > 0:
        result = result + (clib*remotenode)
    return result

if __name__ == '__main__':
    main()
