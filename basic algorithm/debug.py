def filt2(x):
    st = [0] * (x + 1)
    prime = [0] * x
    cnt = 0

    for i in range(2,x+1):
        if not st[i]:
            prime[cnt] = i
            cnt += 1
        j = 0
        while prime[j] <= x / i:
            st[prime[j] * i] = 1
            if i % prime[j] == 0: break
            j += 1
    return cnt
print(filt2(int(input())))