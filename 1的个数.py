n = int(input())

a = list(map(int,input().split()))

def lowbit(x):                        # 找到最低那一位的1
    return x & -x
    
res = []

for i in range(n):
    res.append(0)
    while a[i]:
        a[i] -= lowbit(a[i])          # 每次都把最低位的1减去，通过统计减法次数，计算1的个数
        res[i] += 1
        
print(' '.join(map(str,res)))