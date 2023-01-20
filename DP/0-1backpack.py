import numpy as np
n = 3 #3个物品
v = 5 #五个体积
x = [[3,2,5],[8,5,12]] #记录体积与价值
f = np.zeros((n,v+1),int) #记录中间值f[i][j],含义为前i种物品j背包容量下的最大价值
def maxPrice(x,v):
    for i in range(n):
        for j in range(1,v+1):
            m = 0 #临时最大值
            for h in range(j // x[0][i]+1):
                m = max(m,x[1][i] * h + f[i-1][j-x[0][i]*h])
            f[i][j] = m


maxPrice(x,v)
print(f[n-1][v])


