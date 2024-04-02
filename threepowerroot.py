def root(n):
    l = -10000.000000
    r = 10000.000000
    while (r - l > 1E-8):
        mid = (l + r) / 2
        if mid ** 3 >= n:
            r = mid
        else:
            l = mid

    return '%.6f'%l

n = float(input())
print(root(n))