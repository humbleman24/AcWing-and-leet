N = 100010
n,m,x = list(map(int,input().split()))

a = list(map(int,input().split()))
b = list(map(int,input().split()))

    
i = 0
j = m-1
while i < n:
    while j>=0 and a[i]+b[j]>x:
        j -= 1
    if a[i] + b[j] == x:
        print(i,j)
        break
    i += 1

