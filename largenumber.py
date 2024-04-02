def add(ln,lm):
    out = list()
    t = 0
    i = 0
    while i < len(ln) or i < len(lm):
        if i < len(ln): t += ln[i]
        if i < len(lm): t += lm[i]
        out.append(t%10)
        t = t//10
        i += 1
    if t: out.append(t)
    return out

def subtraction(ln,lm):
    reverse = False           # we need to gurantee that ln is larger than lm, so that we can use the bit-wise substraction
    if len(ln) < len(lm):
        ln, lm = lm, ln
        reverse = True
    elif len(ln) == len(lm):
        i = len(ln) - 1
        while i >= 0:
            if ln[i] > lm[i]:
                break
            elif ln[i] < lm[i]:
                ln, lm= lm, ln
                reverse = True
                break
            i -= 1
    ''' Another way to implement
    if len(ln) != len(lm): reverse = len(ln) < len(lm)
    elif len(ln) == len(lm):
        i = len(ln) - 1
        while i >= 0:
            if ln[i] != lm[i]: reverse = ln[i] < lm[i]
    '''
    out = list()
    i = 0
    while i < len(ln) or i < len(lm):
        if i >= len(lm):
            out.append(ln[i])
        else:
            if ln[i] - lm[i] < 0:               # sometimes forget this
                j = i + 1                       # start with the next bit!
                while ln[j] <= 0:               # keep each bit non-negative! would be a problem when there is no need to substraction, there is no chance to brown 10!
                    ln[j] += 9
                    j += 1
                ln[j] -= 1              
                out.append(10 + ln[i] - lm[i])
            else:
                out.append(ln[i] - lm[i])
        i += 1
    while len(out) > 1 and out[-1] == 0:         # prefix 0s need to be removed
        out.pop(-1)
    '''Another way to implement
    t = 0
    for i in range(len(ln)):
        t = ln[i] - t
        if i < len(lm): t -= lm[i]
        out.append((t+10)%10)
        if t<0: t = 1                             表示借位
        else: t = 0
    '''
    if reverse:
        out.append('-')
    return out

def multilpy(ln,b):
    out = list()
    t = 0
    for i in range(len(ln)):
        t += b * ln[i]
        out.append(t%10)
        t //= 10
    while t != 0:
        out.append(t%10)
        t //= 10
    while len(out)>1 and out[-1] == 0:
        out.pop(-1)
    return out

def divide(ln,b):
    out = list()
    remain = 0
    for i in range(len(ln)-1,-1,-1):
        remain = remain*10 + ln[i]
        out.append(remain//b)
        remain = remain%b
    out.reverse()
    while len(out) > 1 and out[-1] == 0:
        out.pop(-1)
    return (out,remain)


# add and subtract
# n = input()
# m = input()
# ln = list()
# lm = list()
# for i in range(len(n)-1, -1, -1):
#     ln.append(int(n[i]))
# for j in range(len(m)-1, -1, -1):
#     lm.append(int(m[j]))

# out = add(ln,lm)
# out = subtraction(ln,lm)
# for i in range(len(out)-1, -1, -1):
#     print(out[i],end='')


# multiply and divide
# n = input()
# ln = list()
# for i in range(len(n)-1, -1, -1):
#     ln.append(int(n[i]))
# b = int(input())


# out = multilpy(ln,b)
# out,remain = divide(ln,b)
# for i in range(len(out)-1, -1, -1):
#     print(out[i],end='')
# print('\n{}'.format(remain))



