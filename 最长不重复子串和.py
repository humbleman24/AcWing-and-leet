# 双指针算法
# n = int(input())
# a = list(map(int,input().split()))

import time
n = 100000
a = list(map(int,input().split()))

s1 = time.time()
count = 1
k = 0
for i in range(n):
    for j in range(k,i+1):
        ok = True
        for l in range(j,i):
            if a[i] != a[l]:
                continue
            else:
                ok = False
                break
        if ok:
            count = max(count,i-j+1)
            break
        else:
            k = j + 1
            continue

# print(count)
s2 = time.time()
print(s2 - s1)





# n = int(input())
# a = list(map(int,input().split()))
s = [0] * 100010

count = 1
j = 0
for i in range(n):
    s[a[i]] += 1
    while s[a[i]] > 1:             # while 表示要一直找到使得s[a[i]]为1！！
        s[a[j]] -= 1               # 大于1 才要做下面的操作，别理解错了
        j += 1
    count = max(count,i-j+1)

# print(count)
s3 = time.time()
print(s3 - s2)
        
            