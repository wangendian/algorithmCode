import numpy as np

map = np.zeros((16, 16), int)

map[0][1] = 5;map[0][2] = 3
map[1][3] = 1;map[1][4] = 3;map[1][5] = 6
map[2][4] = 8;map[2][5] = 7;map[2][6] = 6
map[3][7] = 6;map[3][8] = 8
map[4][7] = 3;map[4][8] = 5
map[5][8] = 3;map[5][9] = 3
map[6][8] = 8;map[6][9] = 4
map[7][10] = 2;map[7][11] = 2
map[8][11] = 1;map[8][12] = 2
map[9][12] = 3;map[9][13] = 3
map[10][13] = 3;map[10][14] = 5
map[11][13] = 5;map[11][14] = 2
map[12][13] = 6;map[12][14] = 6
map[13][15] = 4
map[14][15] = 3

def printRoute(index,n):
    if(index[int(n)] != 0):
        printRoute(index, index[int(n)])
    if(index[int(n)] == 0):
        print(0,end="")
    else:
        print("-->",index[int(n)],end="")

def minDistance(map):
    f = [float('inf')]*len(map)
    f[0] = 0
    index = np.zeros(len(map),int)
    for i in range(len(map)-1):
        for j in range(i,len(map)):
            if(map[i][j] != 0):
                if(f[j]>(f[i] + map[i][j])):
                    f[j] = f[i] + map[i][j]
                    index[j] = i
    print("最短路径长度为：",f[len(map)-1])
    printRoute(index,len(map)-1)
    print("--> ",len(map)-1)

minDistance(map)


